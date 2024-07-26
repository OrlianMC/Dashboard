from rest_framework import viewsets
from .models import Pais
from .serializers import Pais_Serializer

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = Pais_Serializer