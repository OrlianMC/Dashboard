from rest_framework import viewsets
from .models import Programa
from .serializers import Programa_Serializer

class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = Programa_Serializer