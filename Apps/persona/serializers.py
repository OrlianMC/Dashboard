from rest_framework import serializers
from .models import Persona
      
class Persona_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Persona
        fields = ['idpersona', 'ci', 'nombre', 'apellido', 'sexo']