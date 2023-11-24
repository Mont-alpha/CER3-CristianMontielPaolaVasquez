from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):
    prueba = Evento.objects.all()
    for j in prueba:
        print(j.asociacion)
    return render(request,"anexo2.html")