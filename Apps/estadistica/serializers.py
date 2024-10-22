from rest_framework import serializers

class Doctoral_students_by_knowledge_areaSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    doctorando_count = serializers.IntegerField()
    
class Doctoral_students_by_program_and_areaSerializer(serializers.Serializer):
    facultadarea_idarea__nombre = serializers.CharField()
    programa_idprograma__nombre = serializers.CharField()
    doctorando_count = serializers.IntegerField()