from rest_framework import viewsets
from .models import Areadeconocimiento
from .serializers import Areadeconocimiento_Serializer

class AreadeconocimientoViewSet(viewsets.ModelViewSet):
    queryset = Areadeconocimiento.objects.all()
    serializer_class = Areadeconocimiento_Serializer