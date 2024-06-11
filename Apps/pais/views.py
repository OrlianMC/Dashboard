import json
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from rest_framework.views import APIView
import re

class PaisView(APIView):

    def get(self, request):
        paises = Pais.objects.all()
        serializer = Pais_Serializer(paises, many=True)
        return Response(serializer.data)    

    def post(self, request):
        
        data_in = json.loads(request.body)

        idpais = data_in.get('idpais')
        nombre = data_in.get('nombre')
        codigo = data_in.get('codigo')
        
        validacion = validar_datos(idpais, nombre, codigo)
        if validacion:
            return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        pais = Pais(idpais= idpais, nombre=nombre, codigo=codigo)
        pais.save()

        return Response({"message": "País creado correctamente"}, status=status.HTTP_201_CREATED)

    def put(self, request):
        data_in = json.loads(request.body)
        idpais = data_in.get('idpais')
        
        if idpais is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            pais = get_object_or_404(Pais, idpais=idpais)
            
            nombre = data_in.get('nombre')
            codigo = data_in.get('codigo')
            
            validacion = validar_datos(idpais, nombre, codigo)
            if validacion:
                return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

            pais.nombre = nombre
            pais.codigo = codigo
            pais.save()
        
            return Response({"message": "País modificado correctamente"}, status=status.HTTP_200_OK)
        
        except Pais.DoesNotExist:
            return Response({"message": "El país especificado no existe"}, status=404)

    def delete(self, request):
        idpais = request.data.get('idpais')
        if idpais is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            pais = get_object_or_404(Pais, idpais=idpais)
            pais.delete()
            return Response({"message": "País eliminado"}, status=status.HTTP_200_OK)
        except Pais.DoesNotExist:
            return Response({"message": "El país especificado no existe"}, status=404)
        
def validar_datos(idpais, nombre, codigo):
    errores = []
        
    if not all([idpais, nombre, codigo]):
        errores.append("Faltan campos requeridos")
    
    if len(nombre) > 45:
        errores.append("Campo excede límite de 45 caracteres")
        
    if len(codigo) > 45:
        errores.append("Campo excede límite de 45 caracteres")    

    if re.search(r'\d', nombre):
        errores.append("Cadena contiene números")
        
    if re.search(r'\d', codigo):
        errores.append("Cadena contiene números")
                
    return errores