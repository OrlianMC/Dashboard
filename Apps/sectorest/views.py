import json
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from rest_framework.views import APIView
import re

class SectorestView(APIView):

    def get(self, request):
        sectorest = Sectorest.objects.all()
        serializer = Sectorest_Serializer(sectorest, many=True)
        return Response(serializer.data)    

    def post(self, request):
        
        data_in = json.loads(request.body)

        idsectorest = data_in.get('idsectorest')
        nombre = data_in.get('nombre')
        
        validacion = validar_datos(idsectorest, nombre)
        if validacion:
            return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        sectorest = Sectorest(idsectorest= idsectorest, nombre=nombre)
        sectorest.save()

        return Response({"message": "Sector estratégico creado correctamente"}, status=status.HTTP_201_CREATED)

    def put(self, request):
        data_in = json.loads(request.body)
        idsectorest = data_in.get('idsectorest')
        
        if idsectorest is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            sectorest = get_object_or_404(Sectorest, idsectorest=idsectorest)
            
            nombre = data_in.get('nombre')
            
            validacion = validar_datos(idsectorest, nombre)
            if validacion:
                return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

            sectorest.nombre = nombre
            sectorest.save()
        
            return Response({"message": "Sector estratégico modificado correctamente"}, status=status.HTTP_200_OK)
        
        except Sectorest.DoesNotExist:
            return Response({"message": "El Sector estratégico especificado no existe"}, status=404)

    def delete(self, request):
        idsectorest = request.data.get('idsectorest')
        if idsectorest is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            sectorest = get_object_or_404(Sectorest, idsectorest=idsectorest)
            sectorest.delete()
            return Response({"message": "Sector estratégico eliminado"}, status=status.HTTP_200_OK)
        except Sectorest.DoesNotExist:
            return Response({"message": "El Sector estratégico especificado no existe"}, status=404)
        
def validar_datos(idsectorest, nombre):
    errores = []
        
    if not all([idsectorest, nombre]):
        errores.append("Faltan campos requeridos")
    
    if len(nombre) > 150:
        errores.append("Campo excede límite de 45 caracteres")

    if re.search(r'\d', nombre):
        errores.append("Cadena contiene números")
            
    return errores