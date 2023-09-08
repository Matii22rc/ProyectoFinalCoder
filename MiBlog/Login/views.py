from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import *
from Posteos.views import *
from .models import Avatar

# Create your views here.
def inicio(request):
    avatar=Avatar.objects.filter(user=request.user.id)[0].imagen.url
    posteos_recientes = Posteo.objects.order_by('-fecha_publicacion')[:2]
    return render(request, 'index.html', {'posteos':posteos_recientes, 'avatar':ObtenerAvatar(request)})

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
                return redirect('inicio')
            else:
                return render(request, "login.html", {"mensaje":"Datos incorrectos"})
        else:
            form= AuthenticationForm()
            return render(request, "login.html", {"mensaje":"Formulario erroneo", "form":form})
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
                return redirect('inicio')
            else:
                form=RegistroUsuarioForm()
                return render(request, "registro.html", {"form":form, "mensaje":"Datos erroneos"})
      else:
            form=RegistroUsuarioForm()
            return render(request,"registro.html", {"form":form})

def about(request):
    return render(request, 'about.html', {'avatar':ObtenerAvatar(request)})

@login_required
def editar_perfil(request):
    usuario=request.user
    if request.method == 'POST':
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.first_name = info['first_name']
            usuario.last_name = info['last_name']
            usuario.save()
            return redirect('inicio')
        else:
            return render(request, 'editar_perfil.html', {'formulario':formulario, 'usuario':usuario.username, 'avatar':ObtenerAvatar(request)})
    else:
        formulario = UserEditForm(instance=usuario)
    return render(request, "editar_perfil.html", {"formulario": formulario, 'usuario':usuario.username, 'avatar':ObtenerAvatar(request)})

def ObtenerAvatar(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    if len(avatares) != 0:
        return avatares[0].imagen.url
    else:
        return "media/avatares/avatar_por_defecto.jpg"
