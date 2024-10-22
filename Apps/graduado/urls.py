from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import GraduadoViewSet

router = DefaultRouter()
router.register(r'graduados', GraduadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]