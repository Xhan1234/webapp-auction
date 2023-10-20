from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from user_registration.models import UserProfile  # Import your UserProfile model
from user_registration.forms import EditUserProfileForm  # Import your EditUserProfileForm
from crud.models import Product

def public_profile(request, username):
    vendor_profile = get_object_or_404(UserProfile, username=username)
    products = Product.objects.filter(author=vendor_profile)
    return render(request, 'temp-files/store/index.html', {'vendor_profile': vendor_profile, 'products': products})




@login_required(login_url='user_login')
def personal_profile(request, username):
    user = get_object_or_404(UserProfile, username=username)
    products = Product.objects.filter(author=user)
    product_count = Product.objects.filter(author=user).count()

    is_vendor = user.groups.filter(name='vendor').exists()  # Check if the user is in the 'vendor' group

    return render(request, 'temp-files/customer-dashboard/index.html',
                  {'user': user, 'products': products, 'product_count': product_count, 'is_vendor': is_vendor})


@login_required(login_url='user_login')
def edit_profile(request, username):
    try:
        # Ensure the current user is the one who can edit this profile
        user_profile = UserProfile.objects.get(username=username)
    except UserProfile.DoesNotExist:
        # Handle the case where the requested user profile does not exist or does not belong to the current user
        messages.error(request, 'You do not have permission to edit this profile.')
        return redirect('profile_view')  # Redirect to a suitable view, e.g., user's profile

    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')

            # Check if a 'next' parameter is in the URL
            next_url = request.GET.get('next')
            if next_url and user_profile.is_profile_complete():
                # Redirect the user to the checkout page after profile completion
                return redirect('order_product:checkout')

            return redirect('vendor_user_profile:edit_profile', username=username)  # Redirect to a suitable view, e.g., user's profile
    else:
        # Fetch user data and use it to populate the form
        form = EditUserProfileForm(instance=user_profile)

    # Pass the user_profile data to the template
    context = {
        'form': form,
        'user_data': user_profile,  # This provides user data to populate placeholders in the template
    }

    return render(request, 'temp-files/customer-dashboard/edit_profile.html', context)