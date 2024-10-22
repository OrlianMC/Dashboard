#     idprograma = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=250)
#     sectorest = models.BooleanField()
#     desarrollolocal = models.BooleanField()
#     adistancia = models.BooleanField()
#     estdesarrollomun = models.BooleanField()
#     area_idarea = models.ForeignKey(Area, on_delete=models.CASCADE)
#     areadeconocimiento_idareadeconocimiento = models.ForeignKey(Areadeconocimiento, on_delete=models.CASCADE)

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *
from Apps.area.models import *
from Apps.areadeconocimiento.models import *

class ProgramaTests(APITestCase):
    def setUp(self):
        self.area = Area.objects.create(nombre="Test Area")
        self.areadeconocimiento = Areadeconocimiento.objects.create(nombre="Test Areadeconocimiento")
        
        self.programa = Programa.objects.create(
            nombre="Test Programa",
            sectorest=True,
            desarrollolocal=True,
            adistancia=True,
            estdesarrollomun=True,
            area_idarea=self.area,
            areadeconocimiento_idareadeconocimiento=self.areadeconocimiento
        )
     
    def test_create_programa(self):
        url = reverse('programa-list')
        data = {
            'nombre':'Programa Nuevo',
            'sectorest':True,
            'desarrollolocal':True,
            'adistancia':True,
            'estdesarrollomun':True,
            'area_idarea':self.area.idarea,
            'areadeconocimiento_idareadeconocimiento':self.areadeconocimiento.idareadeconocimiento,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Programa.objects.count(), 2)
        self.assertEqual(Programa.objects.get(idprograma=2).nombre, 'Programa Nuevo')   
    
    def test_get_programa(self):
        url = reverse('programa-detail', args=[self.programa.idprograma])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.programa.nombre)
        
    def test_update_programa(self):
        url = reverse('programa-detail', args=[self.programa.idprograma])
        data = {
            'nombre':'Programa Actualizado',
            'sectorest':True,
            'desarrollolocal':True,
            'adistancia':True,
            'estdesarrollomun':True,
            'area_idarea':self.area.idarea,
            'areadeconocimiento_idareadeconocimiento':self.areadeconocimiento.idareadeconocimiento,
            }
        response = self.client.put(url, data, format='json')
        self.programa.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.programa.nombre, 'Programa Actualizado')
        
    def test_delete_programa(self):
        url = reverse('programa-detail', args=[self.programa.idprograma])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Programa.objects.count(), 0)
        
        
        
        
        # py manage.py test Apps.programa.tests.ProgramaTests