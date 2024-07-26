from rest_framework import viewsets
from .models import Area
from .serializers import Area_Serializer

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = Area_Serializer