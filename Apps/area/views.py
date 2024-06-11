import json
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from rest_framework.views import APIView
import re

class AreaView(APIView):

    def get(self, request):
        areas = Area.objects.all()
        serializer = Area_Serializer(areas, many=True)
        return Response(serializer.data)    

    def post(self, request):
        
        data_in = json.loads(request.body)

        idarea = data_in.get('idarea')
        nombre = data_in.get('nombre')
        
        validacion = validar_datos(idarea, nombre)
        if validacion:
            return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        area = Area(idarea= idarea, nombre=nombre)
        area.save()

        return Response({"message": "Área creada correctamente"}, status=status.HTTP_201_CREATED)

    def put(self, request):
        data_in = json.loads(request.body)
        idarea = data_in.get('idarea')
        
        if idarea is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            area = get_object_or_404(Area, idarea=idarea)
            
            nombre = data_in.get('nombre')
            
            validacion = validar_datos(idarea, nombre)
            if validacion:
                return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

            area.nombre = nombre
            area.save()
        
            return Response({"message": "Área modificada correctamente"}, status=status.HTTP_200_OK)
        
        except Area.DoesNotExist:
            return Response({"message": "El área especificada no existe"}, status=404)

    def delete(self, request):
        idarea = request.data.get('idarea')
        if idarea is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            area = get_object_or_404(Area, idarea=idarea)
            area.delete()
            return Response({"message": "Área eliminada"}, status=status.HTTP_200_OK)
        except Area.DoesNotExist:
            return Response({"message": "El área especificada no existe"}, status=404)
        
def validar_datos(idarea, nombre):
    errores = []
        
    if not all([idarea, nombre]):
        errores.append("Faltan campos requeridos")
    
    if len(nombre) > 45:
        errores.append("Campo excede límite de 45 caracteres")

    if re.search(r'\d', nombre):
        errores.append("Cadena contiene números")
            
    return errores