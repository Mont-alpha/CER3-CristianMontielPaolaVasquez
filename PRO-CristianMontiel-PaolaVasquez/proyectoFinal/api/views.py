from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from core.models import Evento
from .serializer import EventoSerializer
from rest_framework.decorators import action
# Create your views here.

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all().order_by("fecha_Inicio") #obtiene desde aqui los datos que van a ser serializados
    serializer_class = EventoSerializer #marco de referencia para entregar el json

    #crud: list -> get , create -> post, retiree -> get con parametro adicional, destroy -> delete , update -> put
'''    def list(self, request):
        serializer = EventoSerializer(self.queryset,many=True)
        return Response(serializer.data)'''


def peticiones(request):

    respuesta = request.get('http://127.0.0.1:8000/api/Evento')
    data = respuesta.json()
    return data