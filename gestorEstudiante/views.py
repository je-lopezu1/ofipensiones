import random
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from gestorEstudiante.logic.logic_estudiante import verificar, asociar_estudiante_curso, crear_estudiante, lista_estudiantes
from ofipensiones.auth0backend import getRole
from django.contrib.auth.decorators import login_required

def verificar_estudiante( nombre_estudiante, apellido_estudiante):
    resultado = verificar(nombre_estudiante, apellido_estudiante)
    return resultado

def asociar (codigo_estudiante, codigo_curso):
    resultado = asociar_estudiante_curso(  codigo_estudiante, codigo_curso)
    return resultado

@login_required
def crear(request):
    role = getRole(request)
    if role == "Administrador":
       return crear_estudiante(request)
    else:
        return HttpResponse("Unauthorized User")

def listar(request):
    return lista_estudiantes(request)

