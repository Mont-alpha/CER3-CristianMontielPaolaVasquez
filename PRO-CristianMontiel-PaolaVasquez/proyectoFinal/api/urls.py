from rest_framework import routers
from django.urls import include,path

from . import views


router = routers.DefaultRouter()
router.register('Evento',views.EventoViewSet)

urlpatterns = [
path('', include(router.urls)),
path('peticion',views.peticiones,name="peticion")
]
