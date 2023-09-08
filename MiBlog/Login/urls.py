from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name="Login"),
    path('register/', register, name="Register"),
    path('logout/', LogoutView.as_view(next_page='Login'), name="Logout"),
    path('about/', about, name="about"),
]