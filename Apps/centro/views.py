from rest_framework import viewsets
from .models import Centro
from .serializers import Centro_Serializer

class CentroViewSet(viewsets.ModelViewSet):
    queryset = Centro.objects.all()
    serializer_class = Centro_Serializer