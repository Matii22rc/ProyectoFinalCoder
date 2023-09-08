from django.shortcuts import render, get_object_or_404, redirect
from .models import Posteo
from .forms import PosteoForm
from django.contrib.auth.decorators import login_required

def lista_posteos(request):
    posteos = Posteo.objects.order_by('-fecha_publicacion')
    return render(request, 'posteos.html', {'posteos': posteos})

def detalle_posteo(request, id):
    posteo = get_object_or_404(Posteo, pk=id)
    return render(request, 'post.html', {'posteo': posteo})

@login_required
def crear_posteo(request):
    if request.method == 'POST':
        formulario = PosteoForm(request.POST, request.FILES)
        if formulario.is_valid():
            nuevo_posteo = formulario.save(commit=False)
            nuevo_posteo.autor = request.user
            nuevo_posteo.save()
            return redirect('detalle_posteo', posteo_id=nuevo_posteo.id)
    else:
        formulario = PosteoForm()
    return render(request, 'crear_posteo.html', {'formulario': formulario})

@login_required
def editar_posteo(request, id):
    if request.user.is_staff:
        posteo=Posteo.objects.get(id=id)
        if request.method == 'POST':
            formulario=PosteoForm(request.POST, request.FILES, instance=posteo)
            if formulario.is_valid():
                posteo.save()
                return redirect('detalle_posteo', id=id)
        formulario=PosteoForm(instance=posteo)
        return render(request, 'editar_posteo.html', {'formulario':formulario,'posteo':posteo})    

@login_required
def borrar_posteo(request, id):
    posteo = get_object_or_404(Posteo, id=id)
    posteo.delete()

    return redirect('posteos')