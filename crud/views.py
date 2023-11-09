import io
from PIL import Image
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from .forms import CreateProductForm
from .models import Product
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required


# Create Product
@login_required
def add_products(request):
    # Check if the user belongs to the "vendor" group
    vendor_group = Group.objects.get(name='vendor')
    is_vendor = vendor_group in request.user.groups.all()

    if is_vendor:
        print("User is a vendor")
        # Your existing code for handling vendor user
    else:
        print("User is not a vendor")
        # Your code for non-vendor users

    if request.method == 'POST':
        if is_vendor:  # Check if the user is a vendor before processing the form
            form = CreateProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.author = request.user
                product.created_at = timezone.now()

                # Open the uploaded image using Pillow
                image = Image.open(product.image)

                # Resize the image while maintaining the aspect ratio
                max_width = 1000
                max_height = 800
                image.thumbnail((max_width, max_height))

                # Create an in-memory file-like object to save the resized image
                output_io = io.BytesIO()
                image.save(output_io, format='JPEG')

                # Create a new InMemoryUploadedFile with the resized image
                resized_image = InMemoryUploadedFile(
                    output_io, None, product.image.name, 'image/jpeg',
                    output_io.getbuffer().nbytes, None
                )

                # Assign the resized image back to the product
                product.image = resized_image

                # Now save the product to the database
                product.save()

                # Construct the URL for the product detail page
                product_detail_url = reverse('product_detail', kwargs={'product_slug': product.slug})

                return redirect(product_detail_url)
        else:
            return redirect('vendor_user_profile:personal_profile', username=request.user.username)  # Redirect to a different dashboard for non-vendor users

    else:
        form = CreateProductForm()

    return render(request, 'temp-files/add-remove-products/index.html', {'form': form, 'is_vendor': is_vendor})


# Update Product
@login_required
def update_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)

            # Image processing (same as in add_product)
            image = Image.open(product.image)
            max_width = 1000
            max_height = 800
            image.thumbnail((max_width, max_height))
            output_io = io.BytesIO()
            image.save(output_io, format='JPEG')
            resized_image = InMemoryUploadedFile(
                output_io, None, product.image.name, 'image/jpeg',
                output_io.getbuffer().nbytes, None
            )
            product.image = resized_image

            product.save()
            product_detail_url = reverse('product_detail', kwargs={'product_slug': product.slug})
            return redirect(product_detail_url)
    else:
        form = CreateProductForm(instance=product)
    return render(request, 'temp-files/update_product/index.html', {'form': form, 'product': product})


# Delete Product
@login_required
def delete_product(request, product_slug):
    try:
        product = Product.objects.get(slug=product_slug)
        product.delete()
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    username = request.user.username
    return redirect(reverse('vendor_user_profile:personal_profile', args=[username]))  # Redirect to a product list view after deletion


# Read Product
# views.py
def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    if not product.slug:  # Check if the slug is empty
        raise Http404("Product does not exist")

    # Pass the product title to the context
    product_title = product.title
    product_id = product.id
    return render(request, 'temp-files/product-model/index.html', {'product': product, 'product_title': product_title, 'product_id': product_id})

