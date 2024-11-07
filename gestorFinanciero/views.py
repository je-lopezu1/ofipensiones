import json
from django.shortcuts import render
from django.http import JsonResponse
from gestorFinanciero.logic.logic_financiero import calcular_monto, calcular_matricula

def verificar_monto():
    calcular_monto()

def matricula (codigo_estudiante):
    return calcular_matricula(codigo_estudiante)