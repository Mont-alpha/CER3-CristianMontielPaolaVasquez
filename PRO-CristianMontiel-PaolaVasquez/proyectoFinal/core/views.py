from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):
    filtrarUsuario = SegmentoUsario.objects.all()
    segmentoslistados = Segmento.objects.all()
    data = {"filtro": filtrarUsuario,"segmentoLista": segmentoslistados}
    
    usuariosListados = list()
    for u in filtrarUsuario:
        usuariosListados.append(u.usuario.all())
    data = {"filtro": filtrarUsuario,"segmentoLista": usuariosListados}
    print(type(usuariosListados[0][0]))

    
  
    return render(request,"anexo2.html",data)