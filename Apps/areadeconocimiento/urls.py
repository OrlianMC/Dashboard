from django.urls import path
from .views import *

urlpatterns = [
    path('areadeconocimientos/', AreadeconocimientoView.as_view()),
]