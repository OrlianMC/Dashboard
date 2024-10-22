from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *

class SectorestTests(APITestCase):

    def setUp(self):
        self.sectorest = Sectorest.objects.create(nombre="Test Sectorest")

    def test_create_sectorest(self):
        url = reverse('sectorest-list')
        data = {'nombre': 'sectorest Sectorest'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sectorest.objects.count(), 2)
        self.assertEqual(Sectorest.objects.get(idsectorest=2).nombre, 'sectorest Sectorest')

    def test_get_sectorest(self):
        url = reverse('sectorest-detail', args=[self.sectorest.idsectorest])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.sectorest.nombre)

    def test_update_sectorest(self):
        url = reverse('sectorest-detail', args=[self.sectorest.idsectorest])
        data = {'nombre': 'Sectorest Actualizado'}
        response = self.client.put(url, data, format='json')
        self.sectorest.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.sectorest.nombre, 'Sectorest Actualizado')

    def test_delete_sectorest(self):
        url = reverse('sectorest-detail', args=[self.sectorest.idsectorest])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Sectorest.objects.count(), 0)
        
        
        
        
        # py manage.py test Apps.sectorest.tests.SectorestTests