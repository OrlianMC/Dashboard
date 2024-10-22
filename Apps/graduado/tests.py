from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *
from Apps.area.models import *
from Apps.centro.models import *
from Apps.pais.models import *
from Apps.sectorest.models import *
from Apps.areadeconocimiento.models import *
from Apps.persona.models import *
  
class GraduadoTests(APITestCase):
    def setUp(self):
        self.sectorest = Sectorest.objects.create(nombre="Test Sectorest")
        self.pais = Pais.objects.create(nombre="Test Pais", codigo="Test Codigo")
        self.centro = Centro.objects.create(nombre="Test Centro", organismo="Test Organismo")
        self.area = Area.objects.create(nombre="Test Area")
        self.areadeconocimiento = Areadeconocimiento.objects.create(nombre="Test Areadeconocimiento")
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
        
        self.graduado = Graduado.objects.create(
          fechadefensa="2024-10-22",
          persona_idpersona=self.persona,
          facultadarea_idarea=self.area,
          areadeconocimiento_idareadeconocimiento=self.areadeconocimiento
        )
        
    def test_create_graduado(self):
        url = reverse('graduado-list')
        data = {
            'fechadefensa': '2024-10-21',
            'persona_idpersona': self.persona.idpersona,
            'facultadarea_idarea': self.area.idarea,
            'areadeconocimiento_idareadeconocimiento': self.areadeconocimiento.idareadeconocimiento,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Graduado.objects.count(), 2)
        self.assertEqual(Graduado.objects.last().fechadefensa.strftime('%Y-%m-%d'), '2024-10-21')
        
    def test_get_graduado(self):
        url = reverse('graduado-detail', args=[self.graduado.idgraduado])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['fechadefensa'], self.graduado.fechadefensa)
        
    def test_update_graduado(self):
        url = reverse('graduado-detail', args=[self.graduado.idgraduado])
        data = {
            'fechadefensa': '2024-10-20',
            'persona_idpersona': self.persona.idpersona,
            'facultadarea_idarea': self.area.idarea,
            'areadeconocimiento_idareadeconocimiento': self.areadeconocimiento.idareadeconocimiento,
            }
        response = self.client.put(url, data, format='json')
        self.persona.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Graduado.objects.last().fechadefensa.strftime('%Y-%m-%d'), '2024-10-20')
        
    def test_delete_graduado(self):
        url = reverse('graduado-detail', args=[self.graduado.idgraduado])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Graduado.objects.count(), 0)
        
        
        
        
        # py manage.py test Apps.graduado.tests.GraduadoTests