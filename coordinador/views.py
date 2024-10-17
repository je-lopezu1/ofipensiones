import json
from django.shortcuts import render
from django.http import JsonResponse
from coordinador.logic.logic_coordinador import verificar as verificar_general
from coordinador.logic.logic_coordinador import asociar as asociar_general
from django.http import HttpResponse

def verificar(request):
    resultado = verificar_general(request)
    return (resultado)

def asociar(request):
    resultado = asociar_general(request)
    return (resultado)

def healthCheck(request):
    return HttpResponse('ok')