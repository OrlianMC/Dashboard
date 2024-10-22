from django.urls import path
from .views import *

urlpatterns = [
    path('estadisticas/', EstadisticaView.as_view(), name='dashboard-data'),
]