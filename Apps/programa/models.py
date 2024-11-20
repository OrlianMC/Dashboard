from django.db import models
from Apps.centro.models import *
from Apps.areadeconocimiento.models import *

# Create your models here.
class Programa(models.Model):
    idprograma = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250)
    sectorest = models.BooleanField()
    desarrollolocal = models.BooleanField()
    adistancia = models.BooleanField()
    estdesarrollomun = models.BooleanField()
    centro_idcentro = models.ForeignKey(Centro, on_delete=models.CASCADE)
    areadeconocimiento_idareadeconocimiento = models.ForeignKey(Areadeconocimiento, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre