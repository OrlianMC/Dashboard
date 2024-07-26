from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import DoctorandoViewSet

router = DefaultRouter()
router.register(r'doctorandos', DoctorandoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]