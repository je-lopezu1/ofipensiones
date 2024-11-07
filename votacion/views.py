import json
from django.http import JsonResponse
from django.shortcuts import render
from votacion.logic.logic_votacion import realizar_votacion as quorum

def votacion(request):
    if request.method == 'POST':
        try:
            # Cargar los datos del cuerpo de la solicitud JSON
            data = json.loads(request.body)

            # Si data es un solo objeto, convertirlo a una lista con un solo elemento
            if isinstance(data, dict):
                data = [data]  # Convertir a lista

            # Verificar que 'data' sea una lista
            if not isinstance(data, list):
                return JsonResponse({'error': 'Se esperaba un objeto o un arreglo de objetos.'}, status=400)

            resultados = []

            # Iterar sobre cada objeto en la lista y enviar a quorum
            for item in data:
                # Extraer los datos del estudiante y del curso
                codigo_estudiante = item.get('codigo_estudiante')
                codigo_curso = item.get('codigo_curso')

                # Verificar que se hayan proporcionado los datos requeridos
                if not (codigo_estudiante and codigo_curso):
                    resultados.append({
                        'error': 'Faltan datos obligatorios en uno de los objetos',
                        'data': item
                    })
                    continue

                # Llamar a la función quorum para cada item
                resultado_quorum = quorum(codigo_estudiante, codigo_curso)

                # Agregar el resultado a la lista de resultados
                resultados.append(resultado_quorum)

            # Retornar todos los resultados
            return JsonResponse({'resultados': resultados})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)

