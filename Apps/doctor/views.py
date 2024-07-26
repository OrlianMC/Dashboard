from rest_framework import viewsets
from .models import Doctor
from .serializers import Doctor_Serializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = Doctor_Serializer