from rest_framework import viewsets
from .models import Doctorando
from .serializers import Doctorando_Serializer

class DoctorandoViewSet(viewsets.ModelViewSet):
    queryset = Doctorando.objects.all()
    serializer_class = Doctorando_Serializer