from django.shortcuts import render
from django.http import JsonResponse
from gestorUsuarios.logic.logic_usuarios import verificar_af

def verificar_padre(id_padre, nombre, nombre_estudiante):
    resultado = verificar_af(id_padre, nombre, nombre_estudiante)
    return resultado

