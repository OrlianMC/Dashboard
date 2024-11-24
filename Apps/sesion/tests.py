# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.test import APIClient
# from Apps.usuario.models import * 
# from django.urls import reverse
# import json

# def get_jwt_token(user):
#     refresh = RefreshToken.for_user(user)
#     return str(refresh.access_token)

# class SesionTest(TestCase):
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(username='testuser', password='testpass', email='test@gmail.com', role=Usuario.ADMIN)
#         self.client = APIClient()
#         self.jwt_token = get_jwt_token(self.user)
#         self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.jwt_token}')

#     def test_login_success(self): 
#         response = self.client.post(reverse('login'), 
#         data=json.dumps({'username': 'testuser', 'password': 'testpass'}), content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('token', response.json())
#         self.assertIn('access', response.json()['token'])

#     def test_login_fail(self):
#         response = self.client.post(reverse('login'), 
#         data=json.dumps({'username': 'testuser', 'password': 'wrongpass'}), content_type='application/json')
#         self.assertEqual(response.status_code, 401)
#         self.assertEqual(response.json(), {'message': 'Login failed'})
        
#     def test_login_not_post_method(self):
#         response = self.client.get(reverse('login'))
#         self.assertEqual(response.status_code, 405)

#     def test_logout_success(self):
#         self.client.login(username='testuser', password='testpass')
#         response = self.client.post(reverse('logout'))
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), {'message': 'Logout successful'})
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Usuario

def get_jwt_token(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)

class UsuarioTests(APITestCase):

    def setUp(self):
        self.admin_user = Usuario.objects.create_user(
            username='adminuser',
            password='adminpass',
            email='admin@example.com',
            role=Usuario.ADMIN
        )
        self.manager_user = Usuario.objects.create_user(
            username='manageruser',
            password='managerpass',
            email='manager@example.com',
            role=Usuario.MANAGER
        )
        self.regular_user = Usuario.objects.create_user(
            username='regularuser',
            password='userpass',
            email='user@example.com'
        )
        
        self.url = reverse('usuario-list')
        self.admin_token = get_jwt_token(self.admin_user)
        self.manager_token = get_jwt_token(self.manager_user)
        self.regular_token = get_jwt_token(self.regular_user)

    def authenticate(self, token):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_create_usuario_as_admin(self):
        self.authenticate(self.admin_token)
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass',
            'role': Usuario.USER
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Usuario.objects.count(), 4)  # 3 existing + 1 new

    def test_create_usuario_as_non_admin(self):
        self.authenticate(self.regular_token)
        data = {
            'username': 'newuser2',
            'email': 'newuser2@example.com',
            'password': 'newpass',
            'role': Usuario.USER
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_usuarios(self):
        self.authenticate(self.admin_token)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # 3 usuarios creados

    def test_update_usuario_as_admin(self):
        self.authenticate(self.admin_token)
        user_to_update = self.regular_user
        url = reverse('usuario-detail', args=[user_to_update.id])
        data = {
            'username': 'updateduser',
            'email': 'updateduser@example.com',
            'password': 'updatedpass',
            'role': Usuario.MANAGER
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user_to_update.refresh_from_db()
        self.assertEqual(user_to_update.username, 'updateduser')
        self.assertEqual(user_to_update.role, Usuario.MANAGER)

    def test_delete_usuario_as_admin(self):
        self.authenticate(self.admin_token)
        user_to_delete = self.manager_user
        url = reverse('usuario-detail', args=[user_to_delete.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Usuario.objects.count(), 2)  # 2 remaining usuarios

    def test_update_usuario_as_non_admin(self):
        self.authenticate(self.regular_token)
        user_to_update = self.manager_user
        url = reverse('usuario-detail', args=[user_to_update.id])
        data = {
            'username': 'hackeduser',
            'email': 'hackeduser@example.com',
            'role': Usuario.ADMIN
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_usuario_as_non_admin(self):
        self.authenticate(self.regular_token)
        user_to_delete = self.manager_user
        url = reverse('usuario-detail', args=[user_to_delete.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)