from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *

class CentroTests(APITestCase):

    def setUp(self):
        self.centro = Centro.objects.create(nombre="Test Centro", organismo="Test Organismo")

    def test_create_centro(self):
        url = reverse('centro-list')
        data = {
            'nombre': 'Nuevo Centro',
            'organismo': 'Nuevo Organismo'
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Centro.objects.count(), 2)
        self.assertEqual(Centro.objects.get(idcentro=2).nombre, 'Nuevo Centro')

    def test_get_centro(self):
        url = reverse('centro-detail', args=[self.centro.idcentro])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.centro.nombre)
        self.assertEqual(response.data['organismo'], self.centro.organismo)
        
    def test_update_centro(self):
        url = reverse('centro-detail', args=[self.centro.idcentro])
        data = {
            'nombre': 'Centro Actualizado',
            'organismo': 'Organismo Actualizado'
            }
        response = self.client.put(url, data, format='json')
        self.centro.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.centro.nombre, 'Centro Actualizado')
        self.assertEqual(self.centro.organismo, 'Organismo Actualizado')

    def test_delete_centro(self):
        url = reverse('centro-detail', args=[self.centro.idcentro])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Centro.objects.count(), 0)
        
        
        
        
        # py manage.py test Apps.centro.tests.CentroTests