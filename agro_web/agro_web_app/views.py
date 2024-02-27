from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse

def inicio(request):
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def contacto(request):
    plantilla = loader.get_template('contacto.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def servicios(request):
    plantilla = loader.get_template('servicios.html')
    documento = plantilla.render()
    return HttpResponse(documento)