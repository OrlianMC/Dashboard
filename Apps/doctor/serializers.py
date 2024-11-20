from rest_framework import serializers
from .models import *
      
class Doctor_Serializer(serializers.ModelSerializer):
    persona_idpersona = serializers.PrimaryKeyRelatedField(queryset=Persona.objects.all())
    facultadarea_idarea = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())
    areadeconocimiento_idareadeconocimiento = serializers.PrimaryKeyRelatedField(queryset=Areadeconocimiento.objects.all())
    
    class Meta:
        model = Doctor
        fields = ['iddoctor', 'persona_idpersona', 'facultadarea_idarea', 'areadeconocimiento_idareadeconocimiento']