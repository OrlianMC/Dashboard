from rest_framework import serializers
from .models import *
      
class Pais_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pais
        fields = ['idpais','nombre', 'codigo']