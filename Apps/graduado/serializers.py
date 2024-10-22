from rest_framework import serializers
from .models import *
from Apps.persona.models import *
from Apps.area.models import *
from Apps.areadeconocimiento.models import *

class Graduado_Serializer(serializers.ModelSerializer):
    persona_idpersona = serializers.PrimaryKeyRelatedField(queryset=Persona.objects.all())
    facultadarea_idarea = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())
    areadeconocimiento_idareadeconocimiento = serializers.PrimaryKeyRelatedField(queryset=Areadeconocimiento.objects.all())
    
    class Meta:
        model = Graduado
        fields = [
            'idgraduado',
            'fechadefensa',
            'persona_idpersona',
            'facultadarea_idarea',
            'areadeconocimiento_idareadeconocimiento'
        ]