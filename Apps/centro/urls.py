from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CentroViewSet

router = DefaultRouter()
router.register(r'centros', CentroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]