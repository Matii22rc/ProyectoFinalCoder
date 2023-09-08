from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/login/', login_request, name="Login"),
    path('accounts/signup/', register, name="Register"),
    path('accounts/editar_perfil/', editar_perfil, name="EditarPerfil"),
    path('logout/', LogoutView.as_view(next_page='Login'), name="Logout"),
    path('about/', about, name="about"),
]