from django.db import models

# Create your models here.
class Sectorest(models.Model):
    idsectorest = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nombre