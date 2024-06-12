from django.urls import path
from .views import *

urlpatterns = [
    path('doctores/', DoctorView.as_view()),
]