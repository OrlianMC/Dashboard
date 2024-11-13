from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from Apps.doctor.models import *
from Apps.doctorando.models import *
from Apps.tutor.models import *
from Apps.graduado.models import *
from Apps.persona.models import *
from Apps.programa.models import *
from Apps.areadeconocimiento.models import *
from datetime import date
from django.db.models import Count, Value
from django.db.models.functions import Coalesce


class EstadisticaView(APIView):
    def get(self, request):

        return Response({
            'doctorage': self.get_doctor_age(),
            'doctoral_studentage': self.get_doctoral_student_age(),
            'tutorage': self.get_tutor_age(),
            'graduadoage': self.get_graduado_age(),
            'doctoral_students_by_knowledge_area' : self.get_doctoral_students_by_knowledge_area(),
            'doctoral_students_by_program_and_area' : self.get_doctoral_students_by_program_and_area(),
            'doctoral_students_and_graduates_by_year': self.get_doctoral_students_and_graduates_by_year(),
        })

    def get_doctor_age(self):
        doctors = Doctor.objects.select_related('persona_idpersona').all()
        total_age = 0
        valid_count = 0
    
        for doctor in doctors:
            try:
                age = self.calculate_age(doctor.persona_idpersona.ci)
                total_age += age
                valid_count += 1
            except ValueError:
                continue
            
        average_age = total_age / valid_count if valid_count > 0 else 0
        return int(average_age)

    def get_doctoral_student_age(self):
        doctoral_students = Doctorando.objects.select_related('persona_idpersona').all()
        total_age = 0
        valid_count = 0
    
        for doctoral_student in doctoral_students:
            try:
                age = self.calculate_age(doctoral_student.persona_idpersona.ci)
                total_age += age
                valid_count += 1
            except ValueError:
                continue
            
        average_age = total_age / valid_count if valid_count > 0 else 0
        return int(average_age)

    def get_tutor_age(self):
        tutors = Tutor.objects.select_related('doctor_iddoctor__persona_idpersona').all()
        total_age = 0
        valid_count = 0
    
        for tutor in tutors:
            try:
                age = self.calculate_age(tutor.doctor_iddoctor.persona_idpersona.ci)
                total_age += age
                valid_count += 1
            except ValueError:
                continue
            
        average_age = total_age / valid_count if valid_count > 0 else 0
        return int(average_age)
    
    def get_graduado_age(self):
        graduates = Graduado.objects.select_related('persona_idpersona').all()
        total_age = 0
        valid_count = 0
    
        for graduate in graduates:
            try:
                age = self.calculate_age(graduate.persona_idpersona.ci)
                total_age += age
                valid_count += 1
            except ValueError:
                continue
            
        average_age = total_age / valid_count if valid_count > 0 else 0
        return int(average_age)
    
    def calculate_age(self, ci):
        current_year = date.today().year

        if len(ci) >= 2:
            birth_year = int(ci[:2])
    
            if birth_year <= current_year % 100:
                birth_year += 2000
            else:
                birth_year += 1900

            return current_year - birth_year

        raise ValueError("El carnet de identidad debe tener al menos 2 dígitos.")

    def get_doctoral_students_by_knowledge_area(self):
        results = (
            Areadeconocimiento.objects
            .annotate(doctorando_count=Count('programa__doctorando'))
            .values('nombre', 'doctorando_count')
        )
        serializer = Doctoral_students_by_knowledge_areaSerializer(results, many=True)
        response_data = list(serializer.data)

        return response_data
        
    def get_doctoral_students_by_program_and_area(self):
        
        results = (
        Doctorando.objects
        .values('facultadarea_idarea__nombre', 'programa_idprograma__nombre')
        .annotate(doctorando_count=Count('iddoctorando'))
        )

        serializer = Doctoral_students_by_program_and_areaSerializer(results, many=True)
        response_data = list(serializer.data)
            
        return response_data

    def get_doctoral_students_and_graduates_by_year(self):
        # Contar los doctorandos por año
        doctorando_counts = (
            Doctorando.objects
            .values('fdefensa')
            .annotate(total_doctorandos=Count('iddoctorando'))
        )

        # Contar los graduados por año
        graduado_counts = (
            Graduado.objects
            .values('fechadefensa__year')
            .annotate(total_graduados=Count('idgraduado'))
        )

        # Unir los resultados
        results = {}
        
        for doc in doctorando_counts:
            year = doc['fdefensa']
            results[year] = {
                'total_doctorandos': doc['total_doctorandos'],
                'total_graduados': 0
            }

        for grad in graduado_counts:
            year = grad['fechadefensa__year']
            if year not in results:
                results[year] = {
                    'total_doctorandos': 0,
                    'total_graduados': grad['total_graduados']
                }
            else:
                results[year]['total_graduados'] = grad['total_graduados']

        # Convertir a lista de dicts y ordenar por año
        final_results = [{'año': year, **data} for year, data in results.items()]
        final_results.sort(key=lambda x: x['año'])

        return final_results