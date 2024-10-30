from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ADMIN = 'admin'
    MANAGER = 'manager'
    USER = 'user'
    
    ROLES = [
        (ADMIN, 'Administrador'),
        (MANAGER, 'Gerente'),
        (USER, 'Usuario'),
    ]

    role = models.CharField(max_length=10, choices=ROLES, default=USER)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_manager(self):
        return self.role == self.MANAGER

    @property
    def is_user(self):
        return self.role == self.USER