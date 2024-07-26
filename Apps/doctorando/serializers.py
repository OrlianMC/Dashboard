from rest_framework import serializers
from .models import Doctorando
from Apps.persona.models import *
from Apps.programa.models import *
      
class Doctorando_Serializer(serializers.ModelSerializer):
    persona_idpersona = serializers.PrimaryKeyRelatedField(queryset=Persona.objects.all())
    facultadarea_idarea = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())
    programa_idprograma = serializers.PrimaryKeyRelatedField(queryset=Programa.objects.all())
    sectorest_idsectorest = serializers.PrimaryKeyRelatedField(queryset=Sectorest.objects.all())
    
    class Meta:
        model = Doctorando
        fields = [
            'iddoctorando', 
            'fdefensa', 
            'fingreso', 
            'temadetesis', 
            'fingles', 
            'fespecialidad', 
            'desarrollolocal', 
            'persona_idpersona',
            'facultadarea_idarea',
            'programa_idprograma', 
            'sectorest_idsectorest'
        ]