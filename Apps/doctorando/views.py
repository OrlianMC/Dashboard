import json
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from rest_framework.views import APIView
import re

class DoctorandoView(APIView):

    def get(self, request):
        doctorando = Doctorando.objects.all()
        serializer = Doctorando_Serializer(doctorando, many=True)
        return Response(serializer.data)    

    def post(self, request):
        
        data_in = json.loads(request.body)

        iddoctorando = data_in.get('iddoctorando')
        fdefensa = data_in.get('fdefensa')
        fingreso = data_in.get('fingreso')
        temadetesis = data_in.get('temadetesis')
        fingles = data_in.get('fingles')
        fespecialidad = data_in.get('fespecialidad')
        desarrollolocal = data_in.get('desarrollolocal')
        persona_idpersona = data_in.get('persona_idpersona')
        facultadarea_idarea = data_in.get('facultadarea_idarea')
        programa_idprograma = data_in.get('programa_idprograma')
        sectorest_idsectorest = data_in.get('sectorest_idsectorest')
        
        validacion = validar_datos(
            iddoctorando,
            fdefensa,
            fingreso,
            temadetesis, 
            fingles,
            fespecialidad,
            desarrollolocal,
            persona_idpersona,
            facultadarea_idarea,
            programa_idprograma,
            sectorest_idsectorest            
            )
        
        if validacion:
            return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        persona_idpersona_objects = get_object_or_404(Persona, idpersona = persona_idpersona)
        facultadarea_idarea_objects = get_object_or_404(Area, idarea = facultadarea_idarea)
        programa_idprograma_objects = get_object_or_404(Programa, idprograma = programa_idprograma)
        sectorest_idsectorest_objects = get_object_or_404(Sectorest, idsectorest = sectorest_idsectorest)
        
        existe = Doctorando.objects.filter(iddoctorando=iddoctorando).exists()
        if not existe:
            doctorando = Doctorando(
                iddoctorando = iddoctorando,
                fdefensa = fdefensa,
                fingreso = fingreso,
                temadetesis = temadetesis, 
                fingles = fingles,
                fespecialidad = fespecialidad,
                desarrollolocal = desarrollolocal,
                persona_idpersona = persona_idpersona_objects,
                facultadarea_idarea = facultadarea_idarea_objects,
                programa_idprograma = programa_idprograma_objects,
                sectorest_idsectorest = sectorest_idsectorest_objects
            )
            doctorando.save()
            return Response({"message": "Doctorando insertado correctamente"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Doctorando existente"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            
    def put(self, request):
        data_in = json.loads(request.body)
        iddoctorando = data_in.get('iddoctorando')
        
        if iddoctorando is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            doctorando = get_object_or_404(Doctorando, iddoctorando=iddoctorando)
            
            fdefensa = data_in.get('fdefensa')
            fingreso = data_in.get('fingreso')
            temadetesis = data_in.get('temadetesis')
            fingles = data_in.get('fingles')
            fespecialidad = data_in.get('fespecialidad')
            desarrollolocal = data_in.get('desarrollolocal')
            persona_idpersona = data_in.get('persona_idpersona')
            facultadarea_idarea = data_in.get('facultadarea_idarea')
            programa_idprograma = data_in.get('programa_idprograma')
            sectorest_idsectorest = data_in.get('sectorest_idsectorest')
            
            validacion = validar_datos(
                iddoctorando,
                fdefensa,
                fingreso,
                temadetesis, 
                fingles,
                fespecialidad,
                desarrollolocal,
                persona_idpersona,
                facultadarea_idarea,
                programa_idprograma,
                sectorest_idsectorest            
                )
            
            if validacion:
                return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

            persona_idpersona_objects = get_object_or_404(Persona, idpersona = persona_idpersona)
            facultadarea_idarea_objects = get_object_or_404(Area, idarea = facultadarea_idarea)
            programa_idprograma_objects = get_object_or_404(Programa, idprograma = programa_idprograma)
            sectorest_idsectorest_objects = get_object_or_404(Sectorest, idsectorest = sectorest_idsectorest)
            
            doctorando.fdefensa = fdefensa
            doctorando.fingreso = fingreso
            doctorando.temadetesis = temadetesis
            doctorando.fingles = fingles
            doctorando.fespecialidad = fespecialidad
            doctorando.desarrollolocal = desarrollolocal
            doctorando.persona_idpersona = persona_idpersona_objects,
            doctorando.facultadarea_idarea = facultadarea_idarea_objects,
            doctorando.programa_idprograma = programa_idprograma_objects,
            doctorando.sectorest_idsectorest = sectorest_idsectorest_objects
            doctorando.save()
        
            return Response({"message": "Doctorando modificado correctamente"}, status=status.HTTP_200_OK)
        
        except Doctorando.DoesNotExist:
            return Response({"message": "El doctorando especificado no existe"}, status=404)

    def delete(self, request):
        iddoctorando = request.data.get('iddoctorando')
        
        if iddoctorando is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            doctorando = get_object_or_404(Doctorando, iddoctorando=iddoctorando)
            doctorando.delete()
            return Response({"message": "Doctorando eliminado"}, status=status.HTTP_200_OK)
        except Doctorando.DoesNotExist:
            return Response({"message": "El doctorando especificado no existe"}, status=404)
        
def validar_datos(iddoctorando, fdefensa, fingreso, temadetesis, fingles, fespecialidad, desarrollolocal, persona_idpersona, facultadarea_idarea, programa_idprograma, sectorest_idsectorest):
    errores = []
        
    if not all([iddoctorando, fdefensa, fingreso, temadetesis, fingles, fespecialidad, desarrollolocal, persona_idpersona, facultadarea_idarea, programa_idprograma, sectorest_idsectorest]):
        errores.append("Faltan campos requeridos")
            
    return errores