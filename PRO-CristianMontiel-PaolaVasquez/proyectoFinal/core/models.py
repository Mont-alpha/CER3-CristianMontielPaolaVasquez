from django.db import models

# Create your models here.



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
    segmentoEleccion = (
        (1,"Comunidad USM"),
        (2,"Estudiante"),
        (3,"Profesor"),
        (4,"Jefe de Carrera")
                        )
    tipo = models.IntegerField(choices=descripcion,default=1) 
    segmento = models.IntegerField(choices=segmentoEleccion)

