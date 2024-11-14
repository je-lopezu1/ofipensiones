"""ofipensiones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from gestorUsuarios.views import verificar_padre
from gestorEstudiante.views import verificar_estudiante
from coordinador.views import verificar
from coordinador.views import healthCheck
from coordinador.views import asociar
from coordinador.views import monto
from coordinador.views import crear_curso
from gestorPersistencia.views import pruebasSeguridad
from gestorPersistencia.views import eliminarCursos
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('verificar/', verificar, name='verificar'),
    path('asociar/', asociar, name='asociar'),
    path('health-check/', healthCheck, name='healthCheck'),
    path('monto/', monto, name='votacion'),
    path('health/', views.health_check, name='health'),
    path('crear-curso/', crear_curso, name='crear-curso'),
    path('pruebas-seguridad/', pruebasSeguridad, name='pruebas-seguridad'),
    path('eliminar-curso/', eliminarCursos, name='eliminar-curso'),


]
