from django.urls import path
from .views import *

urlpatterns = [
    path('doctores/', TutorView.as_view()),
]