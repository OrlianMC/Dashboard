from rest_framework import serializers
from .models import *
      
class Programa_Serializer(serializers.ModelSerializer):
    centro_idcentro = serializers.PrimaryKeyRelatedField(queryset=Centro.objects.all())
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
            'centro_idcentro',
            'areadeconocimiento_idareadeconocimiento'
            ]