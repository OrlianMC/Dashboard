from django.urls import path
from .views import *

urlpatterns = [
    path('paises/', PaisView.as_view()),
]