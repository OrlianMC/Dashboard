from django.urls import path
from .views import *

urlpatterns = [
    path('tutores/', TutorView.as_view()),
]