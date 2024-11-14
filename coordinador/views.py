import json
from django.shortcuts import render
from django.http import JsonResponse
from coordinador.logic.logic_coordinador import verificar as verificar_general
from coordinador.logic.logic_coordinador import asociar as asociar_general
from coordinador.logic.logic_coordinador import calcular_matricula as calcular
from coordinador.logic.logic_coordinador import crearCurso
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

def verificar(request):
    resultado = verificar_general(request)
    return (resultado)

def asociar(request):
    resultado = asociar_general(request)
    return (resultado)

def healthCheck(request):
    return HttpResponse('ok')

def crear_curso(request):
    resultado = crearCurso(request)
    return (resultado)

@require_http_methods(["GET", "POST"])
def monto(request):
    print("Método de la solicitud:", request.method)
    if request.method == "GET":
        resultado = calcular(request)
        return resultado
    elif request.method == "POST":
        return JsonResponse({"error": "Método POST no está soportado para esta operación."}, status=405)

