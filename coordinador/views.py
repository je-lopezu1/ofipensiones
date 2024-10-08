import json
from django.shortcuts import render
from django.http import JsonResponse
from coordinador.logic.logic_coordinador import verificar as verificar_general

def verificar(request):
    resultado = verificar_general(request)
    return (resultado)