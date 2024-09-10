from django.db import models

# Create your models here.

class Mensajes(models.Model):
    texto_del_mensaje = models.TextField()
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    fecha_de_envio = models.DateTimeField("Fecha y hora de envio ", auto_now_add= True)

def __str__(self):
    return f'Mensaje de {self.remitente.username} a {self.destinatario.username}'
