from rest_framework import serializers
from .models import Doctorando
      
class Doctorando_Serializer(serializers.ModelSerializer):
    persona_idpersona = serializers.CharField()
    facultadarea_idarea = serializers.CharField()
    programa_idprograma = serializers.CharField()
    sectorest_idsectorest = serializers.CharField()
    
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