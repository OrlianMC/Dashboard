from rest_framework import serializers
from .models import *
      
class Centro_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Centro
        fields = ['idcentro','nombre', 'organismo']