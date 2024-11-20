from django.db import models

# Create your models here.
class Area(models.Model):
    idarea = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45, default='new row')
    
    def __str__(self) :
        return self.nombre