from rest_framework import viewsets
from .models import Tutor
from .serializers import Tutor_Serializer

class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = Tutor_Serializer