from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *
from Apps.area.models import *
from Apps.centro.models import *
from Apps.pais.models import *
from Apps.sectorest.models import *

class PersonaTests(APITestCase):
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

    def test_create_persona(self):
        url = reverse('persona-list')
        data = {
            'ci': '02042545789',
            'nombre': 'Juan2',
            'apellido': 'Pérez2',
            'sexo': 'M',
            'plantillaarea_idarea': self.area.idarea,
            'pais_idpais': self.pais.idpais,
            'centro_idcentro': self.centro.idcentro,
            'sectorest_idsectorest': self.sectorest.idsectorest,
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Persona.objects.count(), 2)
        self.assertEqual(Persona.objects.get(idpersona=2).nombre, 'Juan2')

    def test_get_persona(self):
        url = reverse('persona-detail', args=[self.persona.idpersona])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.persona.nombre)
        
    def test_update_persona(self):
        url = reverse('persona-detail', args=[self.persona.idpersona])
        data = {
            'ci': '02042545789',
            'nombre': 'Juan2 Actualizado',
            'apellido': 'Pérez2 Actualizado',
            'sexo': 'M',
            'plantillaarea_idarea': self.area.idarea,
            'pais_idpais': self.pais.idpais,
            'centro_idcentro': self.centro.idcentro,
            'sectorest_idsectorest': self.sectorest.idsectorest,
            }
        response = self.client.put(url, data, format='json')
        self.persona.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.persona.nombre, 'Juan2 Actualizado')

    def test_delete_persona(self):
        url = reverse('persona-detail', args=[self.persona.idpersona])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Persona.objects.count(), 0)
        
        
        
        
        # py manage.py test Apps.persona.tests.PersonaTests