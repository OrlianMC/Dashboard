from django.db import models

# Create your models here.
class Area(models.Model):
    idarea = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    
    def __str__(self) :
        return self.nombre