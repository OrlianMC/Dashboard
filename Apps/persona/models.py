from django.db import models

class Persona(models.Model):
    idpersona = models.IntegerField(auto_created=True, primary_key=True)
    ci = models.CharField(max_length=11, unique=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    sexo = models.CharField(max_length=45)
    # plantillaarea_idarea
    # pais_idpais
    # centro_idcentro
    # sectorest_idsectorest
    
    def __str__(self) :
        return self.nombre +" "+ self.apellido
