# from rest_framework import serializers
# from .models import Usuario
# from rest_framework.exceptions import ValidationError

# class UsuarioListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Usuario
#         fields = ['id', 'username', 'email', 'role']

# class UsuarioCreateSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=False)
    
#     class Meta:
#         model = Usuario
#         fields = ['id', 'username', 'email', 'password', 'role']
#         read_only_fields = ['id']

#     def validate_username(self, value):
#         if self.instance is None:  # Caso de creación
#             if Usuario.objects.filter(username=value).exists():
#                 raise ValidationError("El nombre de usuario ya está en uso.")
#         else:  # Caso de actualización
#             if Usuario.objects.filter(username=value).exclude(pk=self.instance.pk).exists():
#                 raise ValidationError("El nombre de usuario ya está en uso.")
#         return value

#     def validate_email(self, value):
#         if self.instance is None:  # Caso de creación
#             if Usuario.objects.filter(email=value).exists():
#                 raise ValidationError("El correo electrónico ya está en uso.")
#         else:  # Caso de actualización
#             if Usuario.objects.filter(email=value).exclude(pk=self.instance.pk).exists():
#                 raise ValidationError("El correo electrónico ya está en uso.")
#         return value

#     def create(self, validated_data):
#         user = Usuario(**validated_data)
#         user.set_password(validated_data['password'])  # Encriptar la contraseña
#         user.save()
#         return user

#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.email = validated_data.get('email', instance.email)
#         instance.role = validated_data.get('role', instance.role)

#         # Solo establecer la contraseña si se proporciona
#         if 'password' in validated_data and validated_data['password']:
#             instance.set_password(validated_data['password'])

#         instance.save()
#         return instance
from rest_framework import serializers
from .models import Usuario
from rest_framework.exceptions import ValidationError

class UsuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'role']

class UsuarioCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password', 'role']
        read_only_fields = ['id']

    def __init__(self, *args, **kwargs):
        # Llamar al inicializador de la clase base
        super().__init__(*args, **kwargs)
        
        # Si estamos actualizando (PUT), hacer que 'password' no sea obligatorio
        if self.instance:
            self.fields['password'].required = False

    def validate_username(self, value):
        if self.instance is None:  # Caso de creación
            if Usuario.objects.filter(username=value).exists():
                raise ValidationError("El nombre de usuario ya está en uso.")
        else:  # Caso de actualización
            if Usuario.objects.filter(username=value).exclude(pk=self.instance.pk).exists():
                raise ValidationError("El nombre de usuario ya está en uso.")
        return value

    def validate_email(self, value):
        if self.instance is None:  # Caso de creación
            if Usuario.objects.filter(email=value).exists():
                raise ValidationError("El correo electrónico ya está en uso.")
        else:  # Caso de actualización
            if Usuario.objects.filter(email=value).exclude(pk=self.instance.pk).exists():
                raise ValidationError("El correo electrónico ya está en uso.")
        return value

    def create(self, validated_data):
        user = Usuario(**validated_data)
        user.set_password(validated_data['password'])  # Encriptar la contraseña
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.role = validated_data.get('role', instance.role)

        # Solo establecer la contraseña si se proporciona
        if 'password' in validated_data and validated_data['password']:
            instance.set_password(validated_data['password'])

        instance.save()
        return instance