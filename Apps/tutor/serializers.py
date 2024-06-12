from rest_framework import serializers
from .models import *
      
class Doctor_Serializer(serializers.ModelSerializer):
    doctor_iddoctor = serializers.CharField()
    doctorando_iddoctorando = serializers.CharField()
    
    class Meta:
        model = Tutor
        fields = ['idtutor', 'doctor_iddoctor', 'doctorando_iddoctorando']