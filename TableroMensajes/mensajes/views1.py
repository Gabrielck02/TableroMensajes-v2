from django.shortcuts import render, get_object_or_404
from .models import Mensajes

# Create your views here.

def mensajes_enviados(request, username):
    mensajes = Mensajes.objects.filter(remitente=username).order_by('-fecha_de_envio')
    return render(request, 'mensajes/mensajes_enviados.html', {'remitente': username, 'mensajes': mensajes})