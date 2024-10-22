from rest_framework import viewsets
from .models import *
from .serializers import Graduado_Serializer

class GraduadoViewSet(viewsets.ModelViewSet):
    queryset = Graduado.objects.all()
    serializer_class = Graduado_Serializer