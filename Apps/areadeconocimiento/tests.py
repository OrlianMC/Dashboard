from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *

class AreadeconocimientoTests(APITestCase):
    
    def setUp(self):
        self.areadeconocimiento = Areadeconocimiento.objects.create(nombre="Test Areadeconocimiento")
        
    def test_create_areadeconocimiento(self):
       url = reverse('areadeconocimiento-list')
       data = {'nombre': 'Nueva Areadeconocimiento'}
       response = self.client.post(url, data, format='json')
       self.assertEqual(response.status_code, status.HTTP_201_CREATED)
       self.assertEqual(Areadeconocimiento.objects.count(), 2)
       self.assertEqual(Areadeconocimiento.objects.get(idareadeconocimiento=2).nombre, 'Nueva Areadeconocimiento')

    def test_get_areadeconocimiento(self):
        url = reverse('areadeconocimiento-detail', args=[self.areadeconocimiento.idareadeconocimiento])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.areadeconocimiento.nombre)
        
    def test_update_areadeconocimiento(self):
        url = reverse('areadeconocimiento-detail', args=[self.areadeconocimiento.idareadeconocimiento])
        data = {'nombre': 'Areadeconocimiento Actualizada'}
        response = self.client.put(url, data, format='json')
        self.areadeconocimiento.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.areadeconocimiento.nombre, 'Areadeconocimiento Actualizada')
    
    def test_delete_areadeconocimiento(self):
        url = reverse('areadeconocimiento-detail', args=[self.areadeconocimiento.idareadeconocimiento])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Areadeconocimiento.objects.count(), 0) 
        
        
        
        
        # py manage.py test Apps.area.tests.AreaTests