from django.shortcuts import render


def home_view(request, destinatario, remitente):
    return render(request, 'mensajes/base.html', {
        'destinatario': destinatario,
        'remitente': remitente
    })