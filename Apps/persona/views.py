import json
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from rest_framework.views import APIView
import re

class PersonaView(APIView):

    def get(self, request):
        personas = Persona.objects.all()
        serializer = Persona_Serializer(personas, many=True)
        return Response(serializer.data)    

    def post(self, request):
        
        data_in = json.loads(request.body)

        idpersona = data_in.get('idpersona')
        ci = data_in.get('ci')
        nombre = data_in.get('nombre')
        apellido = data_in.get('apellido')
        sexo = data_in.get('sexo')
        
        validacion = validar_datos(idpersona, ci, nombre, apellido, sexo)
        if validacion:
            return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        persona = Persona(idpersona= idpersona, ci=ci, nombre=nombre, apellido=apellido, sexo=sexo)
        persona.save()

        return Response({"message": "Persona creada correctamente"}, status=status.HTTP_201_CREATED)

    def put(self, request):
        data_in = json.loads(request.body)
        idpersona = data_in.get('idpersona')
        
        if idpersona is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            persona = get_object_or_404(Persona, idpersona=idpersona)
            
            ci = data_in.get('ci')
            nombre = data_in.get('nombre')
            apellido = data_in.get('apellido')
            sexo = data_in.get('sexo')
            
            validacion = validar_datos(idpersona, ci, nombre, apellido, sexo)
            if validacion:
                return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

            persona.ci = ci
            persona.nombre = nombre
            persona.apellido = apellido
            persona.sexo = sexo
            persona.save()
        
            return Response({"message": "Persona modificada correctamente"}, status=status.HTTP_200_OK)
        
        except Persona.DoesNotExist:
            return Response({"message": "La persona especificada no existe"}, status=404)

    def delete(self, request):
        idpersona = request.data.get('idpersona')
        if idpersona is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            persona = get_object_or_404(Persona, idpersona=idpersona)
            persona.delete()
            return Response({"message": "Persona eliminada"}, status=status.HTTP_200_OK)
        except Persona.DoesNotExist:
            return Response({"message": "La persona especificada no existe"}, status=404)
        
        
        
def validar_datos(idpersona, ci, nombre, apellido, sexo):
    errores = []
    campos = [nombre, apellido, sexo]
        
    if not all([idpersona, ci, nombre, apellido, sexo]):
        errores.append("Faltan campos requeridos")
        
    for item in campos:
            
        if len(item) > 45:
            errores.append("Campo excede límite de 45 caracteres")

        if re.search(r'\d', item):
            errores.append("Cadena contiene números")
            
    if re.search(r'[a-zA-Z]', ci):
        errores.append("Cadena contiene letras")
        
    try:
        # Validar la longitud de la cadena
        if len(ci) != 11:
            errores.append("Carnet de identidad incorrecto")

        # Extraer los componentes de la fecha
        anio = ci[:2]
        mes = ci[2:4]
        dia = ci[4:6]

        # Validar los componentes de la fecha
        if not (1 <= int(mes) <= 12):
            errores.append("El mes debe estar entre 1 y 12")
        if not (1 <= int(dia) <= 31):
            errores.append("El día debe estar entre 1 y 31")

    except Exception as e:
        # Manejar la excepción
        return Response("Error al validar la fecha: {}".format(str(e)))
        
    return errores