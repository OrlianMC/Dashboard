from rest_framework import serializers
from .models import Persona
      
class Persona_Serializer(serializers.ModelSerializer):
    plantillaarea_idarea = serializers.IntegerField()
    pais_idpais = serializers.IntegerField()
    centro_idcentro = serializers.IntegerField()
    sectorest_idsectorest = serializers.IntegerField()
    
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