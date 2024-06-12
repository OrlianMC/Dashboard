import json
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from rest_framework.views import APIView
import re

class ProgramaView(APIView):

    def get(self, request):
        programa = Programa.objects.all()
        serializer = Programa_Serializer(programa, many=True)
        return Response(serializer.data)    

    def post(self, request):
        
        data_in = json.loads(request.body)

        idprograma = data_in.get('idprograma')
        nombre = data_in.get('nombre')
        sectorest = data_in.get('sectorest')
        desarrollolocal = data_in.get('desarrollolocal')
        adistancia = data_in.get('adistancia')
        estdesarrollomun = data_in.get('estdesarrollomun')
        area_idarea = data_in.get('area_idarea')
        areadeconocimiento_idareadeconocimiento = data_in.get('areadeconocimiento_idareadeconocimiento')
        
        validacion = validar_datos(
            idprograma,
            nombre,
            sectorest,
            desarrollolocal, 
            adistancia,
            estdesarrollomun,
            area_idarea,
            areadeconocimiento_idareadeconocimiento)
        
        if validacion:
            return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        area_idarea_objects = get_object_or_404(Area, idarea = area_idarea)
        areadeconocimiento_idareadeconocimento_objects = get_object_or_404(Areadeconocimiento, iddoctorando = areadeconocimiento_idareadeconocimiento)
        
        existe = Programa.objects.filter(idprograma=idprograma).exists()
        if not existe:
            programa = Programa(
                idprograma=idprograma,
                area_idarea=area_idarea_objects,
                areadeconocimiento_idareadeconocimiento=areadeconocimiento_idareadeconocimento_objects)
            programa.save()
            return Response({"message": "Programa insertado correctamente"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Programa existente"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            
    def put(self, request):
        data_in = json.loads(request.body)
        idprograma = data_in.get('idprograma')
        
        if idprograma is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            programa = get_object_or_404(Programa, idprograma=idprograma)
            
            nombre = data_in.get('nombre')
            sectorest = data_in.get('sectorest')
            desarrollolocal = data_in.get('desarrollolocal')
            adistancia = data_in.get('adistancia')
            estdesarrollomun = data_in.get('estdesarrollomun')
            area_idarea = data_in.get('area_idarea')
            areadeconocimiento_idareadeconocimiento = data_in.get('areadeconocimiento_idareadeconocimiento')
            
            validacion = validar_datos(
                idprograma,
                nombre,
                sectorest,
                desarrollolocal, 
                adistancia,
                estdesarrollomun,
                area_idarea,
                areadeconocimiento_idareadeconocimiento)
            
            if validacion:
                return Response({"error": "Datos incorrectos"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

            area_idarea_objects = get_object_or_404(Area, idarea = area_idarea)
            areadeconocimiento_idareadeconocimento_objects = get_object_or_404(Areadeconocimiento, idareadeconocimiento = areadeconocimiento_idareadeconocimiento)
            
            programa.nombre = nombre
            programa.sectorest = sectorest
            programa.desarrollolocal = desarrollolocal
            programa.adistancia = adistancia
            programa.estdesarrollomun = estdesarrollomun
            programa.area_idarea = area_idarea_objects
            programa.areadeconocimiento_idareadeconocimiento = areadeconocimiento_idareadeconocimento_objects
            programa.save()
        
            return Response({"message": "Programa modificado correctamente"}, status=status.HTTP_200_OK)
        
        except Programa.DoesNotExist:
            return Response({"message": "El programa especificado no existe"}, status=404)

    def delete(self, request):
        idprograma = request.data.get('idprograma')
        
        if idprograma is None:
            return Response({'error': 'El campo id es requerido'}, status=400)
        
        try:
            programa = get_object_or_404(Programa, idprograma=idprograma)
            programa.delete()
            return Response({"message": "Programa eliminado"}, status=status.HTTP_200_OK)
        except Programa.DoesNotExist:
            return Response({"message": "El programa especificado no existe"}, status=404)
        
def validar_datos(idprograma, nombre, sectorest, desarrollolocal, adistancia, estdesarrollomun, area_idarea, areadeconocimiento_idareadeconocimiento):
    errores = []
        
    if not all([idprograma, nombre, sectorest, desarrollolocal, adistancia, estdesarrollomun, area_idarea, areadeconocimiento_idareadeconocimiento]):
        errores.append("Faltan campos requeridos")
        
    if len(nombre) > 250:
        errores.append("Campo excede límite de 45 caracteres")

    if re.search(r'\d', nombre):
        errores.append("Cadena contiene números")
            
    return errores