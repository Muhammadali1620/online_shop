import random
from datetime import timedelta
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.utils.timezone import now
from django.shortcuts import render, redirect
from apps.users.models import CustomUser, UserAuthCode
from apps.users.services import send_email_to_user

def register_page(request):
    return render(request, template_name='register.html', context={'error':False})


def send_code_to_email(request):
    email, password, re_password = request.POST.get('email'), request.POST.get('password'), request.POST.get('re_password')

    if not (email and password and re_password):
        messages.error(request, message='Fields not found')
        return redirect('register-page')

    if password != re_password:
        messages.error(request, message='Passwords was not equal!!!')
        return redirect('register-page')

    if CustomUser.objects.filter(email=email).exists():
        messages.error(request, message='Email already registered.')
        return redirect('register-page')

    code = random.randint(1000, 10000)
    send_email_to_user(email, code)
    UserAuthCode.objects.create(email=email, code=code, expire_at=now() + timedelta(minutes=5))

    context = {
        'email': email,
        'password': password,
        'code': '',
        'code_error': '',
        'error_message': '',
    }
    return render(request, 'confirm_email.html', context)


def register_user(request):
    code = request.POST.get('code')
    email = request.POST.get('email')
    password = request.POST.get('password')

    UserAuthCode.objects.filter(expire_at__lte=now()).delete()

    objs = UserAuthCode.objects.filter(code=code, email=email, expire_at__gte=now())
 
    if objs.exists():
        CustomUser.objects.create_user(email=email, password=password)
        objs.delete()
    elif UserAuthCode.objects.filter(email=email, expire_at__gte=now()):
        context = {
            'email': email,
            'password': password,
            'code': code,
            'code_error': 'Code not valid.'
        }
        return render(request, 'confirm_email.html', context)

    else:
        return redirect('register-page')
    return render(request, 'login.html')


def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.error(request, 'There was an error logging in, please try again!')
            return redirect('login_page')
    else:
        return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('home-page')