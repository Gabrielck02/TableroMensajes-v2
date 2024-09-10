from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import Mensajes
from .forms import MensajeForm

class CrearMensajeView(CreateView):
    model = Mensajes
    form_class = MensajeForm
    template_name = 'mensajes/crear_mensaje.html'

    def get_success_url(self):
        # Asumiendo que 'destinatario' es el campo del modelo Mensajes que contiene el username
        return reverse('mensajes_recibidos', kwargs={'username': self.object.destinatario})