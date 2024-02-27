from django.contrib import admin
from django.urls import path
from .views import inicio, contacto, servicios


urlpatterns = [
    path('inicio', inicio, name='Inicio'),
    path('contacto', contacto, name='Contacto'),
    path('servicios', servicios, name='Servicios'),
]
