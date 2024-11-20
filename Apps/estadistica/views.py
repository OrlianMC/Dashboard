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
from django.db.models import Count, Value, Case, When, F, IntegerField
from django.db.models.functions import Coalesce, ExtractYear, Now, Substr


class EstadisticaView(APIView):
    def get(self, request):

        return Response({
            'doctorage': self.get_doctor_age(),
            'doctoral_studentage': self.get_doctoral_student_age(),
            'tutorage': self.get_tutor_age(),
            'graduadoage': self.get_graduado_age(),
            'doctoral_students_by_knowledge_area' : self.get_doctoral_students_by_knowledge_area(),
            'doctor_by_knowledge_area': self.get_doctor_by_knowledge_area(),
            'doctoral_students_by_program_and_area' : self.get_doctoral_students_by_program_and_area(),
            'doctor_by_area_and_knowledge_area': self.get_doctor_by_area_and_knowledge_area(),
            'doctoral_students_and_graduates_by_year': self.get_doctoral_students_and_graduates_by_year(),
            'doctoral_students_and_doctors_by_age_groups': self.get_doctoral_students_and_doctors_by_age_groups()
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
    
    def get_doctor_by_knowledge_area(self):
        results = (
            Areadeconocimiento.objects
            .annotate(doctor_count=Count('doctors'))
            .values('nombre', 'doctor_count')
        )
        serializer = Doctor_by_knowledge_areaSerializer(results, many=True)
        response_data = list(serializer.data)

        return response_data
        
    def get_doctoral_students_by_program_and_area(self):
        
        results = (
        Doctorando.objects
        .values('facultadarea_idarea__codigo', 'programa_idprograma__nombre')
        .annotate(doctorando_count=Count('iddoctorando'))
        )

        serializer = Doctoral_students_by_program_and_areaSerializer(results, many=True)
        response_data = list(serializer.data)
            
        return response_data

    def get_doctor_by_area_and_knowledge_area(self):
        results = (
            Doctor.objects
            .values('facultadarea_idarea__codigo', 'areadeconocimiento_idareadeconocimiento__nombre')
            .annotate(doctor_count=Count('iddoctor'))
            # .order_by('facultadarea_idarea__nombre', 'areadeconocimiento_idareadeconocimiento__nombre')
        )
        serializer = Doctor_by_area_and_knowledge_areaSerializer(results, many=True)
        response_data = list(serializer.data)
            
        return response_data

    def get_doctoral_students_and_graduates_by_year(self):
        doctorando_counts = (
            Doctorando.objects
            .values('fdefensa')
            .annotate(total_doctorandos=Count('iddoctorando'))
        )

        graduado_counts = (
            Graduado.objects
            .values('fechadefensa__year')
            .annotate(total_graduados=Count('idgraduado'))
        )

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
    
    def get_doctoral_students_and_doctors_by_age_groups(self):
        doctoral_students = Doctorando.objects.select_related('persona_idpersona').all()
        doctors = Doctor.objects.select_related('persona_idpersona').all()

        age_groups = {
            '<30': {'doctorandos': 0, 'doctores': 0},
            '31-35': {'doctorandos': 0, 'doctores': 0},
            '36-40': {'doctorandos': 0, 'doctores': 0},
            '41-45': {'doctorandos': 0, 'doctores': 0},
            '46-50': {'doctorandos': 0, 'doctores': 0},
            '51-55': {'doctorandos': 0, 'doctores': 0},
            '56-60': {'doctorandos': 0, 'doctores': 0},
            '61 o más': {'doctorandos': 0, 'doctores': 0},
        }

        for student in doctoral_students:
            try:
                age = self.calculate_age(student.persona_idpersona.ci)
                if age < 30:
                    age_groups['<30']['doctorandos'] += 1
                elif 31 <= age <= 35:
                    age_groups['31-35']['doctorandos'] += 1
                elif 36 <= age <= 40:
                    age_groups['36-40']['doctorandos'] += 1
                elif 41 <= age <= 45:
                    age_groups['41-45']['doctorandos'] += 1
                elif 46 <= age <= 50:
                    age_groups['46-50']['doctorandos'] += 1
                elif 51 <= age <= 55:
                    age_groups['51-55']['doctorandos'] += 1
                elif 56 <= age <= 60:
                    age_groups['56-60']['doctorandos'] += 1
                else:
                    age_groups['61 o más']['doctorandos'] += 1
            except ValueError:
                continue

        for doctor in doctors:
            try:
                age = self.calculate_age(doctor.persona_idpersona.ci)
                if age < 30:
                    age_groups['<30']['doctores'] += 1
                elif 31 <= age <= 35:
                    age_groups['31-35']['doctores'] += 1
                elif 36 <= age <= 40:
                    age_groups['36-40']['doctores'] += 1
                elif 41 <= age <= 45:
                    age_groups['41-45']['doctores'] += 1
                elif 46 <= age <= 50:
                    age_groups['46-50']['doctores'] += 1
                elif 51 <= age <= 55:
                    age_groups['51-55']['doctores'] += 1
                elif 56 <= age <= 60:
                    age_groups['56-60']['doctores'] += 1
                else:
                    age_groups['61 o más']['doctores'] += 1
            except ValueError:
                continue

        results = []
        for rango, counts in age_groups.items():
            results.append({
                'rango_edad': rango,
                'cantidad_doctorandos': counts['doctorandos'],
                'cantidad_doctores': counts['doctores'],
            })

        return results
    
    # def get_doctoral_students_by_age_groups(self):
    #     doctoral_students = Doctorando.objects.select_related('persona_idpersona').all()
        
    #     age_groups = {
    #         '<30': 0,
    #         '31-35': 0,
    #         '36-40': 0,
    #         '41-45': 0,
    #         '46-50': 0,
    #         '51-55': 0,
    #         '56-60': 0,
    #         '61 o más': 0,
    #     }

    #     for student in doctoral_students:
    #         try:
    #             age = self.calculate_age(student.persona_idpersona.ci)
    #             if age < 30:
    #                 age_groups['<30'] += 1
    #             elif 31 <= age <= 35:
    #                 age_groups['31-35'] += 1
    #             elif 36 <= age <= 40:
    #                 age_groups['36-40'] += 1
    #             elif 41 <= age <= 45:
    #                 age_groups['41-45'] += 1
    #             elif 46 <= age <= 50:
    #                 age_groups['46-50'] += 1
    #             elif 51 <= age <= 55:
    #                 age_groups['51-55'] += 1
    #             elif 56 <= age <= 60:
    #                 age_groups['56-60'] += 1
    #             else:
    #                 age_groups['61 o más'] += 1
    #         except ValueError:
    #             continue

    #     results = [{'rango_edad': rango, 'cantidad_doctorandos': count} for rango, count in age_groups.items()]
        
    #     return results