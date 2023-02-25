from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from smm.models import Wallet
from .models import MyUser


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Logged in successfully as {email}')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('smm:home')
        else:
            messages.error(request, 'Invalid Credentials. Please Try Again With Correct Credentials')

    context = {
        'title': 'Login',
        'navbar': 'Sign in',

    }
    return render(request, 'user/login.html', context)


def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('mobile')
        see_user = MyUser.objects.filter(email=email)
        if MyUser.objects.filter(email=email).exists():
            messages.error(request, 'User With Email Already Exists, Please Try Signing in')
            return redirect('user:signup')
        else:
            user = MyUser.objects.create_user(email=email, password=password, phone_number=phone)
            user.save()
            messages.success(request, 'Registered Successfully, Login Now')
            wallet = Wallet(user=user, wallet_balance=0)
            wallet.save()
            return redirect('user:login')

    context = {
        'title': 'Register',
        'navbar': 'Sign up',
    }
    return render(request, 'user/register.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out Successfully')
    return redirect('user:login')
