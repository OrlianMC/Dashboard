from rest_framework import serializers
from .models import *
      
class Sectorest_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sectorest
        fields = ['idsectorest','nombre']