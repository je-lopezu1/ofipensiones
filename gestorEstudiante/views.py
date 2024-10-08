from django.shortcuts import render
from django.http import JsonResponse
from gestorEstudiante.logic.logic_estudiante import verificar

def verificar_estudiante(request, nombre_estudiante, apellido_estudiante):
    resultado = verificar(nombre_estudiante, apellido_estudiante)
    return JsonResponse(resultado)
