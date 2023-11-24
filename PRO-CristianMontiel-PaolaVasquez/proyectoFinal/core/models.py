from typing import Any
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin


# Create your models here.




segmentoEleccion = (
        ("C","Comunidad USM"),
        ("E","Estudiante"),
        ("P","Profesor"),
        ("J","Jefe de Carrera")
                        )

class Segmento(models.Model):
    tipo = models.CharField(choices=segmentoEleccion,max_length=30)  
    def __str__(self):
        return self.tipo
    
class CustomAccountManager(BaseUserManager): #creacion por consola, al usar manage.py createsuperuser -> invocar la funcion create_superuser por haber
    def create_user(self, identifier,email,first_name,last_name,password,**other_fields):
        if not email:
            raise ValueError(_('Ingresa una direccion de correo correcta'))
        
        user = self.model(identifier=identifier,email = self.normalize_email(email), first_name=first_name,last_name=last_name,password=password,**other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,identifier, email,first_name,last_name,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('El super usuario debe tener el is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('El super usuario debe tener el is_superuser=True')
        return self.create_user(identifier,email,first_name,last_name,password,**other_fields) #se toma en cuenta los cambios al agumento other_fields y se invoca la otra funcion con los parametros que se pasan

class UserProfile(AbstractBaseUser,PermissionsMixin):
    identifier  = models.CharField(_("Nombre usuario"), max_length=50,default="",unique=True)
    email = models.EmailField(_('correo'),unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    register_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    objects = CustomAccountManager()
    USERNAME_FIELD = 'identifier' #un atributo va ser elegido para ser nombre , pero no se puede usar para otros uso como required
    REQUIRED_FIELDS = ['first_name','last_name','email']


class Evento(models.Model):
    fecha_Inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
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
    asociacion = models.ManyToManyField(Segmento)
    tipo = models.IntegerField(choices=tipoEleccion,default=1) 
    def __str__(self) -> str:
        return self.titulo
    



