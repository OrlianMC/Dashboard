import json
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from rest_framework.views import APIView
import re

class DoctorView(APIView):

    def get(self, request):
        doctor = Doctor.objects.all()
        serializer = Doctor_Serializer(doctor, many=True)
        return Response(serializer.data)    

    def post(self, request):
        
        data_in = json.loads(request.body)

        iddoctor = data_in.get('iddoctor')
        persona_idpersona = data_in.get('persona_idpersona')
        facultadarea_idarea = data_in.get('facultadarea_idarea')
        
        validacion = validar_datos(iddoctor, persona_idpersona, facultadarea_idarea)
        if validacion:
            return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        persona_idpersona_objects = get_object_or_404(Persona, idpersona = persona_idpersona)
        facultadarea_idarea_objects = get_object_or_404(Area, idarea = facultadarea_idarea)
        
        existe = Doctor.objects.filter(iddoctor=iddoctor).exists()
        if not existe:
            doctor = Doctor(iddoctor=iddoctor, persona_idpersona=persona_idpersona_objects, facultadarea_idarea=facultadarea_idarea_objects)
            doctor.save()
            return Response({"message": "Doctor insertado correctamente"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Doctor existente"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            
    def put(self, request):
        data_in = json.loads(request.body)
        iddoctor = data_in.get('iddoctor')
        
        if iddoctor is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            doctor = get_object_or_404(Doctor, iddoctor=iddoctor)
            
            persona_idpersona = data_in.get('persona_idpersona')
            facultadarea_idarea = data_in.get('facultadarea_idarea')
            
            validacion = validar_datos(iddoctor, persona_idpersona, facultadarea_idarea)
            if validacion:
                return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

            persona_idpersona_objects = get_object_or_404(Persona, idpersona = persona_idpersona)
            facultadarea_idarea_objects = get_object_or_404(Area, idarea = facultadarea_idarea)
        
            doctor.persona_idpersona = persona_idpersona_objects
            doctor.facultadarea_idarea = facultadarea_idarea_objects
            doctor.save()
        
            return Response({"message": "Doctor modificado correctamente"}, status=status.HTTP_200_OK)
        
        except Doctor.DoesNotExist:
            return Response({"message": "El doctor especificado no existe"}, status=404)

    def delete(self, request):
        iddoctor = request.data.get('iddoctor')
        if iddoctor is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            doctor = get_object_or_404(Doctor, iddoctor=iddoctor)
            doctor.delete()
            return Response({"message": "Doctor eliminado"}, status=status.HTTP_200_OK)
        except Doctor.DoesNotExist:
            return Response({"message": "El doctor especificado no existe"}, status=404)
        
def validar_datos(iddoctor, persona_idpersona, facultadarea_idarea):
    errores = []
        
    if not all([iddoctor, persona_idpersona, facultadarea_idarea]):
        errores.append("Faltan campos requeridos")
            
    return errores