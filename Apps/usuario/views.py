from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Usuario
from .serializers import *
from .permissions import IsAdminOrReadOnly

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return UsuarioListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return UsuarioCreateSerializer
        return super().get_serializer_class()