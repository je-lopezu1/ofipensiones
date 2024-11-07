import requests
from django.conf import settings
from django.http import JsonResponse


def realizar_votacion(request,codigo_estudiante, codigo_curso):
    votos_positivos = 0
    
    for nodo_url in settings.NODES:
        try:
            # Enviar la solicitud al nodo
            response = requests.get(f"{nodo_url}?estudiante_id={codigo_estudiante}&materia_id={codigo_curso}")
            if response.status_code == 200 and response.json().get("resultado") == "OK":
                votos_positivos += 1
        except requests.RequestException:
            continue  

    # Verificar si se alcanzó el quórum
    resultado = votos_positivos >= 2
    
    # Devolver el resultado
    return JsonResponse({"resultado": "Exitoso" if resultado else "Fallido"})