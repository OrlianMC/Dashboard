"""
URL configuration for dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sesion/', include('Apps.sesion.urls')),
    path('usuario/', include('Apps.usuario.urls')),
    path('persona/', include('Apps.persona.urls')),
    path('area/', include('Apps.area.urls')),
    path('centro/', include('Apps.centro.urls')),
    path('pais/', include('Apps.pais.urls')),
    path('sectorest/', include('Apps.sectorest.urls')), 
    path('areadeconocimiento/', include('Apps.areadeconocimiento.urls')),
    path('doctor/', include('Apps.doctor.urls')),
    path('tutor/', include('Apps.tutor.urls')),
    path('programa/', include('Apps.programa.urls')),
    path('doctorando/', include('Apps.doctorando.urls')),
    path('graduado/', include('Apps.graduado.urls')),
    path('estadistica/', include('Apps.estadistica.urls')),
]
