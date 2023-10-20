from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse

def user_login(request):
    if request.user.is_authenticated:
        username = request.user.username
        return redirect('vendor_user_profile:personal_profile', username=username)
    else:
        if request.method == 'POST':
            username_or_email = request.POST.get('reg_username')
            password = request.POST.get('reg_password')

            user = authenticate(request, username=username_or_email, password=password)

            if user is not None and user.is_active:  # Check if the user is active
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect(reverse('vendor_user_profile:personal_profile', args=[user.username]))
            else:
                messages.info(request, 'Username or password is incorrect or the account is inactive.')

    context = {}
    return render(request, 'temp-files/Log_in/index.html', context)
