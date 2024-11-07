import random
from django.shortcuts import render
from django.http import JsonResponse
from gestorEstudiante.logic.logic_estudiante import verificar, asociar_estudiante_curso, nodo_respuesta

def verificar_estudiante( nombre_estudiante, apellido_estudiante):
    resultado = verificar(nombre_estudiante, apellido_estudiante)
    return resultado

def asociar (codigo_estudiante, codigo_curso):
    resultado = asociar_estudiante_curso(  codigo_estudiante, codigo_curso)
    return resultado

def respuesta_disponibilidad(request):
    return nodo_respuesta(request)
