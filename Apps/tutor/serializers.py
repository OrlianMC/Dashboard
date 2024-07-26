from rest_framework import serializers
from .models import *
      
class Tutor_Serializer(serializers.ModelSerializer):
    doctor_iddoctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    doctorando_iddoctorando = serializers.PrimaryKeyRelatedField(queryset=Doctorando.objects.all())
    
    class Meta:
        model = Tutor
        fields = ['idtutor', 'doctor_iddoctor', 'doctorando_iddoctorando']