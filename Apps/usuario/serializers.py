from rest_framework import serializers
from .models import Usuario

class UsuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'is_admin', 'is_manager']
        
class UsuarioCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password', 'is_admin', 'is_manager']

    def create(self, validated_data):
        user = Usuario(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)
        instance.is_manager = validated_data.get('is_manager', instance.is_manager)

        # Si se proporciona una nueva contraseña, encriptarla
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])

        instance.save()
        return instance