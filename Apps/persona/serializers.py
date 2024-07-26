from rest_framework import serializers
from .models import Persona
from Apps.centro.serializers import *
from Apps.area.serializers import *
from Apps.sectorest.serializers import *
from Apps.pais.serializers import *
      
class Persona_Serializer(serializers.ModelSerializer):
      
    centro_idcentro = serializers.PrimaryKeyRelatedField(queryset=Centro.objects.all())
    plantillaarea_idarea = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())
    pais_idpais = serializers.PrimaryKeyRelatedField(queryset=Pais.objects.all())
    sectorest_idsectorest = serializers.PrimaryKeyRelatedField(queryset=Sectorest.objects.all())
    
    class Meta:
        model = Persona
        fields = [
            'idpersona', 
            'ci', 
            'nombre', 
            'apellido', 
            'sexo', 
            'plantillaarea_idarea', 
            'pais_idpais', 
            'centro_idcentro', 
            'sectorest_idsectorest'
        ]