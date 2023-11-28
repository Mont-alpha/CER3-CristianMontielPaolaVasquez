from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import requests

# Create your views here.


def index(request):
    res = requests.get("http://127.0.0.1:8000/api/Evento/") #peticion get a la api
    guardar = res.json() #lista de elementos
    segmentos = (
        (1,"Comunidad USM"),
        (2,"Estudiante"),
        (3,"Profesor"),
        (4,"Jefe de carrera")
        )
    tipoEleccion = (
        (1,"Vacaciones"), #default
        (2,"Feriado"),
        (3,"Suspension de actividades"),
        (4,"Suspension de actividades PM"),
        (5,"Período Lectivo"),
        (6,"Suspension de evaluciones"),
        (7,"Ceremonia"),
        (8,"EDDA"),
        (9,"Evaluación"),
        (10,"Ayudantias"),
        (11,"Hito Académico"),
        (12,"Secretaría Académica"),
        (13,"OAI")      
            ) #enum
    filtrarUsuario = SegmentoUsario.objects.all()
    #tipos conversion numerica a string
    for j in guardar:
        for k in tipoEleccion:
            if j["tipo"] in k:
                j["tipo"] = k[1]

    for h in guardar:
        listaCambiar = [] #cambia la asociacio de cada objeto a un segmento legible
        for g in h["asociacion"]: #recorro la lista manytomany
            for k in segmentos: 
                if g in k:
                    listaCambiar.append(k[1])
        h["asociacion"] = listaCambiar #hace el cambio
    


    
    usuariosListados = list()
    for u in filtrarUsuario:
        usuariosListados.append(u.usuario.all())
    data = {"filtro": filtrarUsuario,"segmentoLista": usuariosListados,"ListaEventos":guardar}
    

    
  
    return render(request,"anexo2.html",data)

def index2(request,eliminar):
    url = "http://127.0.0.1:8000/api/Evento/"+eliminar+"/"
    eventoDelete = requests.delete(url) #peticion delete a la api

    res = requests.get("http://127.0.0.1:8000/api/Evento/") #peticion get a la api
    guardar = res.json() #lista de elementos
    segmentos = (
        (1,"Comunidad USM"),
        (2,"Estudiante"),
        (3,"Profesor"),
        (4,"Jefe de carrera")
        )
    tipoEleccion = (
        (1,"Vacaciones"), #default
        (2,"Feriado"),
        (3,"Suspension de actividades"),
        (4,"Suspension de actividades PM"),
        (5,"Período Lectivo"),
        (6,"Suspension de evaluciones"),
        (7,"Ceremonia"),
        (8,"EDDA"),
        (9,"Evaluación"),
        (10,"Ayudantias"),
        (11,"Hito Académico"),
        (12,"Secretaría Académica"),
        (13,"OAI")      
            ) #enum
    filtrarUsuario = SegmentoUsario.objects.all()
    #tipos conversion numerica a string
    for j in guardar:
        for k in tipoEleccion:
            if j["tipo"] in k:
                j["tipo"] = k[1]

    for h in guardar:
        listaCambiar = [] #cambia la asociacio de cada objeto a un segmento legible
        for g in h["asociacion"]: #recorro la lista manytomany
            for k in segmentos: 
                if g in k:
                    listaCambiar.append(k[1])
        h["asociacion"] = listaCambiar #hace el cambio
    


    
    usuariosListados = list()
    for u in filtrarUsuario:
        usuariosListados.append(u.usuario.all())
    data = {"filtro": filtrarUsuario,"segmentoLista": usuariosListados,"ListaEventos":guardar}
    

    
  
    return render(request,"anexo2.html",data)