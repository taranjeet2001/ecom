from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from .forms import UserForm, OTPForm
import random

def generate_otp():
    return str(random.randint(100000, 999999))

def view_signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            request.session['otp'] = generate_otp()
            request.session['user_data'] = form.cleaned_data
            email = form.cleaned_data['email']
            send_mail('Your OTP Code', f"Your OTP is {request.session['otp']}", settings.EMAIL_HOST_USER, [email])
            return redirect('verify_otp')
    else:
        form = UserForm()
    return render(request, 'lms/signup.html', {'form': form})

def view_verify_otp(request):
    if request.method == "POST":
        form = OTPForm(request.POST)
        if form.is_valid() and form.cleaned_data['otp'] == request.session.get('otp'):
            user_data = request.session.get('user_data')
            user = User.objects.create_user(username=user_data['username'], email=user_data['email'], password=user_data['password1'])
            del request.session['otp']
            del request.session['user_data']
            messages.success(request, "Signup successful!")
            return redirect('signup')
        else:
            messages.error(request, "Invalid OTP.")
    form = OTPForm()
    return render(request, 'lms/verify_otp.html', {'form': form})