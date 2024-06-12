from django.urls import path
from .views import *

urlpatterns = [
    path('programas/', ProgramaView.as_view()),
]