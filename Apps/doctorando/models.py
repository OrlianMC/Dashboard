from django.db import models
from Apps.persona.models import *
from Apps.area.models import *
from Apps.sectorest.models import *
from Apps.programa.models import *

# Create your models here.
class Doctorando(models.Model):
    iddoctorando = models.AutoField(primary_key=True)
    fdefensa = models.IntegerField(null=True, blank=True)
    fingreso = models.IntegerField(null=True, blank=True)
    temadetesis = models.CharField(max_length=100)
    fingles = models.IntegerField(null=True, blank=True)
    fespecialidad = models.IntegerField(null=True, blank=True)
    desarrollolocal = models.BooleanField(null=True, blank=True)
    persona_idpersona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    facultadarea_idarea = models.ForeignKey(Area, on_delete=models.CASCADE)
    programa_idprograma = models.ForeignKey(Programa, on_delete=models.CASCADE)
    sectorest_idsectorest = models.ForeignKey(Sectorest, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.persona_idpersona.nombre + " " + self.persona_idpersona.apellido)