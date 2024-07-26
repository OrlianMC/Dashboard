from requests import Response
from rest_framework import viewsets
from .models import Centro, Persona
from .serializers import Persona_Serializer
from rest_framework import status

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = Persona_Serializer