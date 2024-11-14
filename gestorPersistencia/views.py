from django.shortcuts import render
from django.http import JsonResponse

from gestorPersistencia.logic.logic_persistencia import pruebas_seguridad, eliminar_cursos

def pruebasSeguridad(request):
    return pruebas_seguridad()

def eliminarCursos(request):
    return eliminar_cursos()