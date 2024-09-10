from django.urls import path
from . import views, views1, views0
from .views2 import CrearMensajeView 
from .views3 import eliminar_mensaje


urlpatterns = [
    path('mensajes/base/', views0.home_view, name='base'),
    path('mensajes/crear/', CrearMensajeView.as_view(), name='crear_mensaje'),  # CBV para crear mensaje
    path('mensajes/recibidos/<str:username>/', views.mensajes_recibidos, name= 'mensajes_recibidos'),
    path('mensajes/enviados/<str:username>/', views1.mensajes_enviados, name= 'mensajes_enviados'),
    path('mensajes/eliminar/<int:pk>/', eliminar_mensaje, name='eliminar_mensaje'),     
]