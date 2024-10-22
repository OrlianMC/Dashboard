from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *
from Apps.area.models import *
from Apps.centro.models import *
from Apps.pais.models import *
from Apps.sectorest.models import *
from Apps.persona.models import *

class DoctorTests(APITestCase):
    def setUp(self):
        self.sectorest = Sectorest.objects.create(nombre="Test Sectorest")
        self.pais = Pais.objects.create(nombre="Test Pais", codigo="Test Codigo")
        self.centro = Centro.objects.create(nombre="Test Centro", organismo="Test Organismo")
        self.area = Area.objects.create(nombre="Test Area")
        self.persona = Persona.objects.create(
            ci="01032456895",
            nombre="Juan",
            apellido="Pérez",
            sexo="M",
            plantillaarea_idarea=self.area,
            pais_idpais=self.pais,
            centro_idcentro=self.centro,
            sectorest_idsectorest=self.sectorest
        )
        self.persona_new = Persona.objects.create(
            ci="02012265896",
            nombre="Armando",
            apellido="Paredes",
            sexo="M",
            plantillaarea_idarea=self.area,
            pais_idpais=self.pais,
            centro_idcentro=self.centro,
            sectorest_idsectorest=self.sectorest
        )
        self.area_new = Area.objects.create(nombre="New Area")
        
        self.doctor = Doctor.objects.create(
            persona_idpersona=self.persona,
            facultadarea_idarea=self.area
        )
        
    def test_create_doctor(self):
        url = reverse('doctor-list')
        data = {
            'persona_idpersona': self.persona_new.idpersona,
            'facultadarea_idarea': self.area_new.idarea
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Doctor.objects.count(), 2)
        self.assertEqual(Doctor.objects.get(iddoctor=2).persona_idpersona, self.persona_new)
        self.assertEqual(Doctor.objects.get(iddoctor=2).facultadarea_idarea, self.area_new)
    
    def test_get_doctor(self):
        url = reverse('doctor-detail', args=[self.doctor.iddoctor])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['persona_idpersona'], self.persona.idpersona)
        
    def test_update_doctor(self):
        url = reverse('doctor-detail', args=[self.doctor.iddoctor])
        data = {
            'persona_idpersona': self.persona.idpersona,
            'facultadarea_idarea': self.area_new.idarea
        }
        response = self.client.put(url, data, format='json')
        self.doctor.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.doctor.facultadarea_idarea, self.area_new)
    
    def test_delete_doctor(self):
        url = reverse('doctor-detail', args=[self.doctor.iddoctor])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Doctor.objects.count(), 0)
        
        
        
        
        # py manage.py test Apps.doctor.tests.DoctorTests