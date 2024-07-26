from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProgramaViewSet

router = DefaultRouter()
router.register(r'programas', ProgramaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]