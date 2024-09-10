from django import forms
from .models import Mensajes

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensajes
        fields = ['remitente', 'destinatario', 'texto_del_mensaje']
        