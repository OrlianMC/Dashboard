import json
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from rest_framework.views import APIView
import re

class AreadeconocimientoView(APIView):

    def get(self, request):
        areadeconocimiento = Areadeconocimiento.objects.all()
        serializer = Areadeconocimiento_Serializer(areadeconocimiento, many=True)
        return Response(serializer.data)    

    def post(self, request):
        
        data_in = json.loads(request.body)

        idareadeconocimiento = data_in.get('idareadeconocimiento')
        nombre = data_in.get('nombre')
        
        validacion = validar_datos(idareadeconocimiento, nombre)
        if validacion:
            return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        existe = Areadeconocimiento.objects.filter(idareadeconocimiento=idareadeconocimiento).exists()
        if not existe:
            areadeconocimiento = Areadeconocimiento(idareadeconocimiento= idareadeconocimiento, nombre=nombre)
            areadeconocimiento.save()
            return Response({"message": "Área de conocimiento creada correctamente"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Área de conocimiento existente"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            
    def put(self, request):
        data_in = json.loads(request.body)
        idareadeconocimiento = data_in.get('idareadeconocimiento')
        
        if idareadeconocimiento is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            areadeconocimiento = get_object_or_404(Areadeconocimiento, idareadeconocimiento=idareadeconocimiento)
            
            nombre = data_in.get('nombre')
            
            validacion = validar_datos(idareadeconocimiento, nombre)
            if validacion:
                return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

            areadeconocimiento.nombre = nombre
            areadeconocimiento.save()
        
            return Response({"message": "Área de conocimiento modificada correctamente"}, status=status.HTTP_200_OK)
        
        except Areadeconocimiento.DoesNotExist:
            return Response({"message": "El área de conocimiento especificada no existe"}, status=404)

    def delete(self, request):
        idareadeconocimiento = request.data.get('idareadeconocimiento')
        if idareadeconocimiento is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            areadeconocimiento = get_object_or_404(Areadeconocimiento, idareadeconocimiento=idareadeconocimiento)
            areadeconocimiento.delete()
            return Response({"message": "Área de conocimiento eliminada"}, status=status.HTTP_200_OK)
        except Areadeconocimiento.DoesNotExist:
            return Response({"message": "El área de conocimiento especificada no existe"}, status=404)
        
def validar_datos(idareadeconocimiento, nombre):
    errores = []
        
    if not all([idareadeconocimiento, nombre]):
        errores.append("Faltan campos requeridos")
    
    if len(nombre) > 45:
        errores.append("Campo excede límite de 45 caracteres")

    if re.search(r'\d', nombre):
        errores.append("Cadena contiene números")
            
    return errores