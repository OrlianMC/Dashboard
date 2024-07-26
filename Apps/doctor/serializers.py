from rest_framework import serializers
from .models import *
      
class Doctor_Serializer(serializers.ModelSerializer):
    persona_idpersona = serializers.PrimaryKeyRelatedField(queryset=Persona.objects.all())
    facultadarea_idarea = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())
    
    class Meta:
        model = Doctor
        fields = ['iddoctor', 'persona_idpersona', 'facultadarea_idarea']