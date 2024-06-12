from rest_framework import serializers
from .models import *
      
class Programa_Serializer(serializers.ModelSerializer):
    area_idarea = serializers.CharField()
    areadeconocimiento_idareadeconocimiento = serializers.CharField()
    
    class Meta:
        model = Programa
        fields = [
            'idprograma',
            'nombre',
            'sectorest',
            'desarrollolocal',
            'adistancia',
            'estdesarrollomun',
            'area_idarea',
            'areadeconocimiento_idareadeconocimiento'
            ]