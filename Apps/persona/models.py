from django.db import models
from Apps.area.models import *
from Apps.centro.models import *
from Apps.pais.models import *
from Apps.sectorest.models import *

class Persona(models.Model):
    idpersona = models.IntegerField(auto_created=True, primary_key=True)
    ci = models.CharField(max_length=11, unique=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    sexo = models.CharField(max_length=45)
    
    plantillaarea_idarea = models.ForeignKey(Area, on_delete=models.CASCADE)
    pais_idpais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    centro_idcentro = models.ForeignKey(Centro, on_delete=models.CASCADE)
    sectorest_idsectorest = models.ForeignKey(Sectorest, on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.nombre +" "+ self.apellido
