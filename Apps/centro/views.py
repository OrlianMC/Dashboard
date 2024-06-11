import json
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from rest_framework.views import APIView
import re

class CentroView(APIView):

    def get(self, request):
        centros = Centro.objects.all()
        serializer = Centro_Serializer(centros, many=True)
        return Response(serializer.data)    

    def post(self, request):
        
        data_in = json.loads(request.body)

        idcentro = data_in.get('idcentro')
        nombre = data_in.get('nombre')
        organismo = data_in.get('organismo')
        
        validacion = validar_datos(idcentro, nombre, organismo)
        if validacion:
            return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        centro = Centro(idcentro= idcentro, nombre=nombre, organismo=organismo)
        centro.save()

        return Response({"message": "Centro creado correctamente"}, status=status.HTTP_201_CREATED)

    def put(self, request):
        data_in = json.loads(request.body)
        idcentro = data_in.get('idcentro')
        
        if idcentro is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            centro = get_object_or_404(Centro, idcentro=idcentro)
            
            nombre = data_in.get('nombre')
            organismo = data_in.get('organismo')
            
            validacion = validar_datos(idcentro, nombre, organismo)
            if validacion:
                return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

            centro.nombre = nombre
            centro.organismo = organismo
            centro.save()
        
            return Response({"message": "Centro modificado correctamente"}, status=status.HTTP_200_OK)
        
        except Centro.DoesNotExist:
            return Response({"message": "El centro especificado no existe"}, status=404)

    def delete(self, request):
        idcentro = request.data.get('idcentro')
        if idcentro is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            centro = get_object_or_404(Centro, idcentro=idcentro)
            centro.delete()
            return Response({"message": "Centro eliminado"}, status=status.HTTP_200_OK)
        except Centro.DoesNotExist:
            return Response({"message": "El centro especificado no existe"}, status=404)
        
def validar_datos(idcentro, nombre, organismo):
    errores = []
        
    if not all([idcentro, nombre]):
        errores.append("Faltan campos requeridos")
    
    if len(nombre) > 45:
        errores.append("Campo excede límite de 45 caracteres")
        
    if len(organismo) > 45:
        errores.append("Campo excede límite de 45 caracteres")    

    if re.search(r'\d', nombre):
        errores.append("Cadena contiene números")
        
    if re.search(r'\d', organismo):
        errores.append("Cadena contiene números")
                
    return errores