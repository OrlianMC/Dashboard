from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PaisViewSet

router = DefaultRouter()
router.register(r'paises', PaisViewSet)

urlpatterns = [
    path('', include(router.urls)),
]