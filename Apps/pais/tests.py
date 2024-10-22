from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *

class PaisTests(APITestCase):

    def setUp(self):
        self.pais = Pais.objects.create(nombre="Test Pais", codigo="Test Codigo")

    def test_create_pais(self):
        url = reverse('pais-list')
        data = {
            'nombre': 'Nuevo Pais',
            'codigo': 'Nuevo Codigo'
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pais.objects.count(), 2)
        self.assertEqual(Pais.objects.get(idpais=2).nombre, 'Nuevo Pais')

    def test_get_pais(self):
        url = reverse('pais-detail', args=[self.pais.idpais])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.pais.nombre)
        self.assertEqual(response.data['codigo'], self.pais.codigo)
        
    def test_update_pais(self):
        url = reverse('pais-detail', args=[self.pais.idpais])
        data = {
            'nombre': 'Pais Actualizado',
            'codigo': 'Codigo Actualizado'
            }
        response = self.client.put(url, data, format='json')
        self.pais.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.pais.nombre, 'Pais Actualizado')
        self.assertEqual(self.pais.codigo, 'Codigo Actualizado')

    def test_delete_pais(self):
        url = reverse('pais-detail', args=[self.pais.idpais])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Pais.objects.count(), 0)
        
        
        
        
        # py manage.py test Apps.pais.tests.PaisTests