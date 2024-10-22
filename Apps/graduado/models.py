from django.db import models
from Apps.persona.models import *
from Apps.area.models import *
from Apps.areadeconocimiento.models import *

# Create your models here.
class Graduado(models.Model):
    idgraduado = models.AutoField(primary_key=True)
    fechadefensa = models.DateField()
    persona_idpersona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    facultadarea_idarea = models.ForeignKey(Area, on_delete=models.CASCADE)
    areadeconocimiento_idareadeconocimiento = models.ForeignKey(Areadeconocimiento, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.persona_idpersona.nombre + " " + self.persona_idpersona.apellido)