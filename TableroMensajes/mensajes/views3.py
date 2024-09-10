from django.shortcuts import get_object_or_404, redirect
from .models import Mensajes

def eliminar_mensaje(request, pk):
    mensaje = get_object_or_404(Mensajes, pk=pk)
    mensaje.delete()
    return redirect('mensajes_recibidos', username=mensaje.destinatario)