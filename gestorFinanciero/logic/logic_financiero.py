import random
import time

from django.http import JsonResponse

def calcular_monto():
    time.sleep(0.1)


def calcular_matricula(codigo_estudiante):
    # Generar un número aleatorio entre 1 millón y 10 millones
    matricula = random.randint(1000000, 10000000)
    
    # Devolver el número aleatorio y el resultado
    return JsonResponse({"matricula": matricula})