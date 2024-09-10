from django.shortcuts import render
from .models import Mensajes

# Create your views here.

def mensajes_recibidos(request, username):
    mensajes = Mensajes.objects.filter(destinatario=username).order_by('-fecha_de_envio')
    return render(request, 'mensajes/mensajes_recibidos.html', {'destinatario': username, 'mensajes': mensajes})
