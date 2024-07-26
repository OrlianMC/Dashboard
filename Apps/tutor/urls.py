from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TutorViewSet

router = DefaultRouter()
router.register(r'tutores', TutorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]