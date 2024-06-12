from django.urls import path
from .views import *

urlpatterns = [
    path('doctorandos/', DoctorandoView.as_view()),
]