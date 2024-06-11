from django.urls import path
from .views import *

urlpatterns = [
    path('sectores/', SectorestView.as_view()),
]