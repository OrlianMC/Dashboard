from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *
from Apps.area.models import *
from Apps.centro.models import *
from Apps.pais.models import *
from Apps.sectorest.models import *
from Apps.doctorando.models import *
from Apps.doctor.models import *
from Apps.programa.models import *
from Apps.areadeconocimiento.models import *
from Apps.persona.models import *

class TutorTests(APITestCase):
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
        self.persona_doc = Persona.objects.create(
            ci="02042569856",
            nombre="Elmo",
            apellido="Nedero",
            sexo="F",
            plantillaarea_idarea=self.area,
            pais_idpais=self.pais,
            centro_idcentro=self.centro,
            sectorest_idsectorest=self.sectorest
        )
        self.persona_doc2 = Persona.objects.create(
            ci="00021245689",
            nombre="Elsi",
            apellido="Garro",
            sexo="M",
            plantillaarea_idarea=self.area,
            pais_idpais=self.pais,
            centro_idcentro=self.centro,
            sectorest_idsectorest=self.sectorest
        )
        self.persona_doc3 = Persona.objects.create(
            ci="02011254785",
            nombre="Elba",
            apellido="Ramos",
            sexo="F",
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
        self.doctor = Doctor.objects.create(
            persona_idpersona=self.persona_doc,
            facultadarea_idarea=self.area
        )
        self.doctor_new = Doctor.objects.create(
            persona_idpersona=self.persona_doc2,
            facultadarea_idarea=self.area
        )
        self.doctor_new2 = Doctor.objects.create(
            persona_idpersona=self.persona_doc3,
            facultadarea_idarea=self.area
        )
        
        self.tutor = Tutor.objects.create(
            doctor_iddoctor=self.doctor,
            doctorando_iddoctorando=self.doctorando
        )
        
        
    def test_create_tutor(self):
        url = reverse('tutor-list')
        data = {
            'doctor_iddoctor': self.doctor_new.iddoctor,
            'doctorando_iddoctorando': self.doctorando.iddoctorando
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tutor.objects.count(), 2)
        self.assertEqual(Tutor.objects.get(idtutor=2).doctor_iddoctor, self.doctor_new)
        
    def test_get_tutor(self):
        url = reverse('tutor-detail', args=[self.tutor.idtutor])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['doctorando_iddoctorando'], self.doctorando.iddoctorando)
        
    def test_update_tutor(self):
        url = reverse('tutor-detail', args=[self.tutor.idtutor])
        data = {
            'doctor_iddoctor': self.doctor_new2.iddoctor,
            'doctorando_iddoctorando': self.doctorando.iddoctorando
        }
        response = self.client.put(url, data, format='json')
        self.tutor.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.tutor.doctor_iddoctor, self.doctor_new2)
        
    def test_delete_tutor(self):
        url = reverse('tutor-detail', args=[self.tutor.idtutor])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tutor.objects.count(), 0)
        
        
        
        
        # py manage.py test Apps.tutor.tests.TutorTests
    