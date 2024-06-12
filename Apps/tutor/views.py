import json
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from rest_framework.views import APIView
import re

class TutorView(APIView):

    def get(self, request):
        tutor = Tutor.objects.all()
        serializer = Doctor_Serializer(tutor, many=True)
        return Response(serializer.data)    

    def post(self, request):
        
        data_in = json.loads(request.body)

        idtutor = data_in.get('idtutor')
        doctor_iddoctor = data_in.get('doctor_iddoctor')
        doctorando_iddoctorando = data_in.get('doctorando_iddoctorando')
        
        validacion = validar_datos(idtutor, doctor_iddoctor, doctorando_iddoctorando)
        if validacion:
            return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        doctor_iddoctor_objects = get_object_or_404(Doctor, iddoctor = doctor_iddoctor)
        doctorando_iddoctorando_objects = get_object_or_404(Doctorando, iddoctorando = doctorando_iddoctorando)
        
        existe = Tutor.objects.filter(idtutor=idtutor).exists()
        if not existe:
            tutor = Tutor(idtutor=idtutor, doctor_iddoctor=doctor_iddoctor_objects, doctorando_iddoctorando=doctorando_iddoctorando_objects)
            tutor.save()
            return Response({"message": "Tutor insertado correctamente"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Tutor existente"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            
    def put(self, request):
        data_in = json.loads(request.body)
        idtutor = data_in.get('idtutor')
        
        if idtutor is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            tutor = get_object_or_404(Tutor, idtutor=idtutor)
            
            doctor_iddoctor = data_in.get('doctor_iddoctor')
            doctorando_iddoctorando = data_in.get('doctorando_iddoctorando')
            
            validacion = validar_datos(idtutor, doctor_iddoctor, doctorando_iddoctorando)
            if validacion:
                return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

            doctor_iddoctor_objects = get_object_or_404(Doctor, iddoctor = doctor_iddoctor)
            doctorando_iddoctorando_objects = get_object_or_404(Doctorando, iddoctorando = doctorando_iddoctorando)
        
            tutor.doctor_iddoctor = doctor_iddoctor_objects
            tutor.doctorando_iddoctorando = doctorando_iddoctorando_objects
            tutor.save()
        
            return Response({"message": "Tutor modificado correctamente"}, status=status.HTTP_200_OK)
        
        except Tutor.DoesNotExist:
            return Response({"message": "El tutor especificado no existe"}, status=404)

    def delete(self, request):
        idtutor = request.data.get('idtutor')
        if idtutor is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            tutor = get_object_or_404(Tutor, idtutor=idtutor)
            tutor.delete()
            return Response({"message": "Tutor eliminado"}, status=status.HTTP_200_OK)
        except Tutor.DoesNotExist:
            return Response({"message": "El tutor especificado no existe"}, status=404)
        
def validar_datos(idtutor, doctor_iddoctor, doctorando_iddoctorando):
    errores = []
        
    if not all([idtutor, doctor_iddoctor, doctorando_iddoctorando]):
        errores.append("Faltan campos requeridos")
            
    return errores