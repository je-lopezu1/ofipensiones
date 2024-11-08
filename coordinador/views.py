import json
from django.shortcuts import render
from django.http import JsonResponse
from coordinador.logic.logic_coordinador import verificar as verificar_general
from coordinador.logic.logic_coordinador import asociar as asociar_general
from coordinador.logic.logic_coordinador import calcular_matricula as calcular
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

@require_http_methods(["GET", "POST"])
def monto(request):
    if request.method == "POST":
        resultado = calcular(request)
        return resultado
    elif request.method == "GET":
        return JsonResponse({"error": "Método GET no está soportado para esta operación."}, status=405)

