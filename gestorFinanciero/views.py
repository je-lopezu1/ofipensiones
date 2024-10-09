from django.shortcuts import render
from django.http import JsonResponse
from gestorFinanciero.logic.logic_financiero import calcular_monto

def verificar_monto():
    calcular_monto()