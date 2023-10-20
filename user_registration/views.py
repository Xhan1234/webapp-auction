from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import UserProfile


def register_user(request):
    if request.user.is_authenticated:
        # If the user is already authenticated, redirect them to their profile.
        return redirect(reverse('vendor_user_profile:personal_profile', args=[request.user.username]))
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password1')
                role = form.cleaned_data.get('role')
                business_name = form.cleaned_data.get('business_name')

                # Create a new UserProfile instance using the custom manager
                user = UserProfile.objects.create_user(username=username, email=email, password=password, role=role,
                                                       business_name=business_name)

                # Assign user to the corresponding group based on their role
                if role == 'customer':
                    group_name = 'customer'
                elif role == 'vendor':
                    group_name = 'vendor'
                else:
                    group_name = 'administrator'

                group, created = Group.objects.get_or_create(name=group_name)
                group.user_set.add(user)

                # Note: You don't need to create another UserProfile instance here.
                # You've already created the user with the CustomUserManager.

                login(request, user)
                messages.success(request, 'Account was created for ' + user.username)
                return redirect('user_login')
        else:
            # If the request method is not POST, display the registration form.
            form = CreateUserForm()

        context = {'form': form}
        return render(request, 'temp-files/register/index.html', context)
