from rest_framework import serializers
from .models import Usuario
from rest_framework.exceptions import ValidationError

class UsuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'role']
        
class UsuarioCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password', 'role']
        read_only_fields = ['id']  # El id no debe ser proporcionado por el cliente

    def validate_username(self, value):
        # Comprobar si el usuario que se está actualizando no es el mismo que el existente
        if self.instance is None:  # Caso de creación
            if Usuario.objects.filter(username=value).exists():
                raise ValidationError("El nombre de usuario ya está en uso.")
        else:  # Caso de actualización
            if Usuario.objects.filter(username=value).exclude(pk=self.instance.pk).exists():
                raise ValidationError("El nombre de usuario ya está en uso.")
        return value

    def validate_email(self, value):
        # Comprobar si el usuario que se está actualizando no es el mismo que el existente
        if self.instance is None:  # Caso de creación
            if Usuario.objects.filter(email=value).exists():
                raise ValidationError("El correo electrónico ya está en uso.")
        else:  # Caso de actualización
            if Usuario.objects.filter(email=value).exclude(pk=self.instance.pk).exists():
                raise ValidationError("El correo electrónico ya está en uso.")
        return value

    def create(self, validated_data):
        user = Usuario(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.role = validated_data.get('role', instance.role)

        # Si se proporciona una nueva contraseña, encriptarla
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])

        instance.save()
        return instance