from rest_framework import serializers as slr
from core.models import Evento,Segmento #extraigo el modelo de la app core



class EventoSerializer(slr.ModelSerializer): #sirve para convertir en json todos los atributos elegidos en el campo fields
    class Meta:
        model = Evento #tabla elegida convertida a json
        fields = "__all__"#campos a utilizar
