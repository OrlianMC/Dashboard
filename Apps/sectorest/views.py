from rest_framework import viewsets
from .models import Sectorest
from .serializers import Sectorest_Serializer

class SectorestViewSet(viewsets.ModelViewSet):
    queryset = Sectorest.objects.all()
    serializer_class = Sectorest_Serializer