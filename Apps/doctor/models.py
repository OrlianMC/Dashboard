from django.db import models
from Apps.persona.models import *
from Apps.area.models import *

# Create your models here.
class Doctor(models.Model):
    iddoctor = models.IntegerField(primary_key=True)
    persona_idpersona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    facultadarea_idarea = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.iddoctor)