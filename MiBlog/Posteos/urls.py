from django.urls import path, include
from .views import *

urlpatterns = [
    path('pages/', lista_posteos, name="posteos"),
    path('crear_posteo/', crear_posteo, name='crear_posteo'),
    path('pages/<id>/', detalle_posteo, name="detalle_posteo"),
    path('editar_posteo/<id>', editar_posteo, name="editar_posteo"),
    path('borrar_posteo/<id>', borrar_posteo, name="borrar_posteo"),
]