from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path("", view_signup, name="signup"),
    path("verify-otp/", view_verify_otp, name="verify_otp"), 
]
