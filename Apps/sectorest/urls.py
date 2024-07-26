from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import SectorestViewSet

router = DefaultRouter()
router.register(r'sectores', SectorestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]