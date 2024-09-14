from django.db import models
from Apps.doctor.models import *
from Apps.doctorando.models import *

# Create your models here.
class Tutor(models.Model):
    idtutor = models.AutoField(primary_key=True)
    doctor_iddoctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctorando_iddoctorando = models.ForeignKey(Doctorando, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.doctor_iddoctor.persona_idpersona.nombre + " tutor de: " + self.doctorando_iddoctorando.persona_idpersona.nombre) 