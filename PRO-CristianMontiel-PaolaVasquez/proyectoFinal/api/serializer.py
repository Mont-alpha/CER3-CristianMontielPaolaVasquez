from rest_framework import serializers
from core.models import Evento #extraigo el modelo de la app core
from django.contrib.auth.models import User


class EventoSerializer(serializers.ModelSerializer): #sirve para convertir en json todos los atributos elegidos en el campo fields
    class Meta:
        model = Evento
        fields = '__all__'

'''class UserSerializar(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password"] #requeridos para el get'''