from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *
from Apps.area.models import *
from Apps.centro.models import *
from Apps.pais.models import *
from Apps.sectorest.models import *

class DoctorandoTests(APITestCase):
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
        self.programa = Programa.objects.create(
            nombre="Test Programa",
            sectorest=True,
            desarrollolocal=True,
            adistancia=True,
            estdesarrollomun=True,
            area_idarea=self.area,
            areadeconocimiento_idareadeconocimiento=self.areadeconocimiento
        )
        
        self.doctorando = Doctorando.objects.create(
            fdefensa="2024",
            fingreso="2020",
            temadetesis="Test",
            fingles="2022",
            fespecialidad="2023",
            desarrollolocal=True,
            persona_idpersona=self.persona,
            facultadarea_idarea=self.area,
            programa_idprograma=self.programa,
            sectorest_idsectorest=self.sectorest
        )
        
    def test_create_doctorando(self):
        url = reverse('doctorando-list')
        data = {
            'fdefensa': '2022',
            'fingreso': '2018',
            'temadetesis': 'Test 2',
            'fingles': '2018',
            'fespecialidad': '2019',
            'desarrollolocal': False,
            'persona_idpersona': self.persona.idpersona,
            'facultadarea_idarea': self.area.idarea,
            'programa_idprograma': self.programa.idprograma,
            'sectorest_idsectorest': self.sectorest.idsectorest,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Doctorando.objects.count(), 2)
        self.assertEqual(Doctorando.objects.get(iddoctorando=2).temadetesis, 'Test 2')
    
    def test_get_doctorando(self):
        url = reverse('doctorando-detail', args=[self.doctorando.iddoctorando])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['temadetesis'], self.doctorando.temadetesis)
        
    def test_update_doctorando(self):
        url = reverse('doctorando-detail', args=[self.doctorando.iddoctorando])
        data = {
            'fdefensa': '2022',
            'fingreso': '2018',
            'temadetesis': 'Test Actualizado',
            'fingles': '2018',
            'fespecialidad': '2019',
            'desarrollolocal': False,
            'persona_idpersona': self.persona.idpersona,
            'facultadarea_idarea': self.area.idarea,
            'programa_idprograma': self.programa.idprograma,
            'sectorest_idsectorest': self.sectorest.idsectorest,
        }
        response = self.client.put(url, data, format='json')
        self.doctorando.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.doctorando.temadetesis, 'Test Actualizado')
        
    def test_delete_doctorando(self):
        url = reverse('doctorando-detail', args=[self.doctorando.iddoctorando])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Doctorando.objects.count(), 0)
        
        
        
        
        # py manage.py test Apps.doctorando.tests.DoctorandoTests