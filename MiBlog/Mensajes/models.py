from django.db import models

class Mensaje(models.Model):
    remitente = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='mensajes_enviados')
    destinatario = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='mensajes_recibidos')
    asunto = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.asunto