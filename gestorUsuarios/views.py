from django.shortcuts import render
from django.http import JsonResponse
from gestorUsuarios.logic.logic_usuarios import verificar_af

def verificar_padre(request, id_padre, nombre):
    resultado = verificar_af(id_padre, nombre)
    return JsonResponse(resultado)

