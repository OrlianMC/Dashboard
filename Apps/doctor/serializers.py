from rest_framework import serializers
from .models import *
      
class Doctor_Serializer(serializers.ModelSerializer):
    persona_idpersona = serializers.CharField()
    facultadarea_idarea = serializers.CharField()
    
    class Meta:
        model = Doctor
        fields = ['iddoctor', 'persona_idpersona', 'facultadarea_idarea']