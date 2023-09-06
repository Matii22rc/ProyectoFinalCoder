from django.shortcuts import render
#para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import *

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            info=form.cleaned_data
            usuario = info['username']
            contraseña = info['password']
            user = authenticate(username= usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "login.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "login.html", {"mensaje":"Formulario erroneo"})
    else:
        form= AuthenticationForm()
        return render(request, "login.html", {"form": form})

def register(request):

      if request.method == "POST":
            form = RegistroUsuarioForm(request.POST)
            if form.is_valid():
                info=form.cleaned_data
                usuario= info['username']
                contraseña=info['password1']
                form.save()
                return render(request,"index.html" , {"mensaje":f"Usuario {usuario} creado"})
            else:
                return render(request, "registro.html", {"mensaje":"Datos erroneos"})
      else:
            form=RegistroUsuarioForm()
            return render(request,"registro.html", {"form":form})

