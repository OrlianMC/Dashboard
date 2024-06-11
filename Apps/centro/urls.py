from django.urls import path
from .views import *

urlpatterns = [
    path('centros/', CentroView.as_view()),
]