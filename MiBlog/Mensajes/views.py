from django.shortcuts import render, get_object_or_404, redirect
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.decorators import login_required
from Login.views import ObtenerAvatar

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        formulario = MensajeForm(request.POST)
        if formulario.is_valid():
            mensaje = formulario.save(commit=False)
            mensaje.remitente = request.user 
            mensaje.save()
            return redirect('mensajes_recibidos')
    else:
        formulario = MensajeForm()
    return render(request, 'enviar_mensaje.html', {'formulario': formulario, 'avatar':ObtenerAvatar(request), "mensajito":"Mensaje enviado!"})

@login_required
def mensajes_recibidos(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha_envio')
    return render(request, 'mensajes_recibidos.html', {'mensajes': mensajes, 'avatar':ObtenerAvatar(request)})

@login_required
def ver_mensaje(request, mensaje_id):
    mensaje = get_object_or_404(Mensaje, pk=mensaje_id)
    return render(request, 'ver_mensaje.html', {'mensaje': mensaje, 'avatar':ObtenerAvatar(request)})