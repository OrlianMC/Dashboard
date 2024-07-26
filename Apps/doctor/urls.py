from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet

router = DefaultRouter()
router.register(r'doctores', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]