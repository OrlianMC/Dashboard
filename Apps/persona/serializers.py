from rest_framework import serializers
from .models import Persona
      
class Persona_Serializer(serializers.ModelSerializer):
    plantillaarea_idarea = serializers.CharField()
    pais_idpais = serializers.CharField()
    centro_idcentro = serializers.CharField()
    sectorest_idsectorest = serializers.CharField()
    
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