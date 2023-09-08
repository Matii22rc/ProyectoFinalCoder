from django.urls import path
from . import views

urlpatterns = [
    path('enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('mensajes_recibidos/', views.mensajes_recibidos, name='mensajes_recibidos'),
    path('mensaje/<int:mensaje_id>/', views.ver_mensaje, name='ver_mensaje'),
]