from rest_framework import serializers
from .models import *
      
class Programa_Serializer(serializers.ModelSerializer):
    area_idarea = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())
    areadeconocimiento_idareadeconocimiento = serializers.PrimaryKeyRelatedField(queryset=Areadeconocimiento.objects.all())
    
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