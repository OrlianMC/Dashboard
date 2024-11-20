from rest_framework import serializers
from .models import *
      
class Area_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Area
        fields = ['idarea','nombre', 'codigo']