from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def template_uno(request):
    plantilla = loader.get_template('vista_uno.html')
    documento = plantilla.render()
    return HttpResponse(documento)

