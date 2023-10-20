from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from crud.models import Product
from .forms import OrderForm
from .models import CartItem, Order, Transaction
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from user_registration.models import UserProfile
from django.urls import reverse

@login_required(login_url='user_login')
def add_cart(request, product_id):
    user = request.user

    # Get the product to add to the cart or return a 404 page if it doesn't exist
    product = get_object_or_404(Product, pk=product_id)

    # Check if the product's author is the same as the logged-in user
    if product.author == user:
        messages.error(request, "You cannot add your own product to the cart.")
    else:
        # Try to get an existing cart item or create a new one
        cart_item, created = CartItem.objects.get_or_create(user=user, product=product)

        if not created:
            # If the item was already in the cart, show a message and don't increase the quantity
            messages.info(request, f"{product.title} is already in your cart.")
        else:
            # If the item is not in the cart, you can add it with quantity 1
            cart_item.quantity = 1
            cart_item.save()
            messages.success(request, f"{product.title} has been added to your cart.")

    return redirect('order_product:cart')


@login_required(login_url='user_login')
def cart(request):
    user = request.user
    cart_items, total_quantity, total_cost, total_cost_with_shipping = get_cart_data(user)

    context = {
        'cart_items': cart_items,
        'total_quantity': total_quantity,
        'total_cost': total_cost,
        'total_cost_with_shipping': total_cost_with_shipping,
    }

    # Render the shopping cart template and return it with the context
    return render(request, 'temp-files/shopping-cart/index.html', context)


@login_required(login_url='user_login')
def delete_cart_item(request, cart_item_id):
    user = request.user

    # Get the cart item to delete
    cart_item = get_object_or_404(CartItem, pk=cart_item_id, user=user)

    if request.method == 'POST':
        # Delete the cart item
        cart_item.delete()
        messages.success(request, f"{cart_item.product.title} has been removed from your cart.")

    return redirect('order_product:cart')



@login_required(login_url='user_login')
@transaction.atomic
def make_purchase(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            user = request.user
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']

            try:
                with transaction.atomic():
                    # Check if the product exists and has enough quantity
                    product = get_object_or_404(Product, pk=product_id)
                    if product.quantity >= quantity:
                        # Deduct quantity from the product
                        product.quantity -= quantity
                        product.save()

                        # Create a purchase record
                        purchase = Order(user=user, product=product, quantity=quantity)
                        purchase.save()

                        # Check if the product quantity is now zero, and update the Buy It Now button text
                        if product.quantity == 0:
                            product.status = False
                        else:
                            product.status = True
                        product.save()

                        # Calculate cart data and pass it to the template
                        cart_items, total_quantity, total_cost, total_cost_with_shipping = get_cart_data(user)
                         # Replace with your logic to generate a transaction ID

                        context = {
                            'form': form,
                            'cart_items': cart_items,
                            'total_quantity': total_quantity,
                            'total_cost': total_cost,
                            'total_cost_with_shipping': total_cost_with_shipping,

                        }

                        messages.success(request, f'You have successfully purchased {quantity} {product.title}.')
                        return render(request, 'temp-files/order-invoice/index.html', context)  # Render the invoice template

                    else:
                        messages.error(request, 'Insufficient quantity available.')
            except Exception as e:
                messages.error(request, 'An error occurred during the purchase process. Please try again later.')
                # You may want to log the exception for debugging purposes
                print(e)
        else:
            print(form.errors)  # Print form errors to the console for debugging
            messages.error(request, 'Invalid form data. Please check your input.')
    else:
        form = OrderForm()

    # Handle rendering when the form is not submitted or when there's an error
    cart_items, total_quantity, total_cost, total_cost_with_shipping = get_cart_data(request.user)
    context = {
        'form': form,
        'cart_items': cart_items,
        'total_quantity': total_quantity,
        'total_cost': total_cost,
        'total_cost_with_shipping': total_cost_with_shipping,

    }
    # Debugging


    return render(request, 'temp-files/order-invoice/index.html', context)




@login_required(login_url='user_login')
def checkout(request):
    user = request.user
    user_profile = UserProfile.objects.get(username=user.username)

    if not user_profile.is_profile_complete():
        # Set a message to be displayed on the 'edit_profile' page
        messages.error(request, "Please complete your profile before making a purchase.")
        redirect_url = reverse('vendor_user_profile:edit_profile', args=[user.username])
        redirect_url += f'?next={reverse("order_product:checkout")}'  # Include the 'next' parameter
        return redirect(redirect_url)

    user_data = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'phone': user.phone,
        'state': user.state,
        'city': user.city,
        'street': user.street,
        'zip_code': user.zip_code,
        'postal_code': user.postal_code,
        'house': user.house,
    }

    cart_items, total_quantity, total_cost, total_cost_with_shipping = get_cart_data(user)

    context = {
        'user_data': user_data,
        'total_quantity': total_quantity,
        'cart_items': cart_items,
        'total_cost': total_cost,
        'total_cost_with_shipping': total_cost_with_shipping,
    }

    return render(request, 'temp-files/checkout-page/index.html', context)


def get_cart_data(user):
    # Retrieve cart items for the user
    cart_items = CartItem.objects.filter(user=user)

    # Calculate the total quantity of items in the cart
    total_quantity = sum(cart_item.quantity for cart_item in cart_items)

    # Calculate the total cost of the products in the cart
    total_cost = sum(Decimal(cart_item.product.price) * cart_item.quantity for cart_item in cart_items)

    total_cost_with_shipping = total_cost + Decimal('20.00')

    return cart_items, total_quantity, total_cost, total_cost_with_shipping




def generate_invoice_pdf(request):
    # Retrieve the completed transaction based on the transaction_id

    # Retrieve user information (e.g., name, address) from the user object
    user = request.user
    user_data = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'phone': user.phone,
        'state': user.state,
        'city': user.city,
        'street': user.street,
        'zip_code': user.zip_code,
        'postal_code': user.postal_code,
        'house': user.house,
    }

    # Get cart data (you can implement the get_cart_data function)
    cart_items, total_quantity, total_cost, total_cost_with_shipping = get_cart_data(user)

    # Calculate the total price for each item in the cart
    for item in cart_items:
        item.total_price = item.quantity * item.product.price

    # Prepare the context for the PDF template
    context = {
        'user_data': user_data,
        'total_quantity': total_quantity,
        'cart_items': cart_items,
        'total_cost': total_cost,
        'total_cost_with_shipping': total_cost_with_shipping,
    }

    # Load the HTML template
    template = get_template('temp-files/pdf_invoice_generator/index.html')

    # Render the template with the context
    html = template.render(context)

    # Create a PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    # Generate the PDF using ReportLab
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response



