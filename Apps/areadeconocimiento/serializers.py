from rest_framework import serializers
from .models import *
      
class Areadeconocimiento_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Areadeconocimiento
        fields = ['idareadeconocimiento','nombre']