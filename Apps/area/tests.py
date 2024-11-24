from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *

class AreaTests(APITestCase):

    def setUp(self):
        self.area = Area.objects.create(nombre="Test Area", codigo="TA")

    def test_create_area(self):
        url = reverse('area-list')
        data = {'nombre': 'Nueva Area', 'codigo': 'New A'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Area.objects.count(), 2)
        self.assertEqual(Area.objects.get(idarea=2).nombre, 'Nueva Area')

    def test_get_area(self):
        url = reverse('area-detail', args=[self.area.idarea])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.area.nombre)

    def test_update_area(self):
        url = reverse('area-detail', args=[self.area.idarea])
        data = {'nombre': 'Area Actualizada', 'codigo': 'New B'}
        response = self.client.put(url, data, format='json')
        self.area.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.area.nombre, 'Area Actualizada')
        self.assertEqual(self.area.codigo, 'New B')

    def test_delete_area(self):
        url = reverse('area-detail', args=[self.area.idarea])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Area.objects.count(), 0)
        
        
        
        
        # py manage.py test Apps.area.tests.AreaTests