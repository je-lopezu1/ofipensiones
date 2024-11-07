from django.http import JsonResponse
import json
from gestorEstudiante.views import verificar_estudiante as verificar_estudiante
from gestorEstudiante.views import asociar as asociar_estudiante_curso
from gestorUsuarios.views import verificar_padre as verificar_padre
from gestorFinanciero.views import verificar_monto as verificar_monto
from gestorFinanciero.views import matricula 
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def verificar(request):
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

            # Iterar sobre cada objeto en la lista
            for item in data:
                # Extraer los datos del estudiante y del padre
                nombre_estudiante = item.get('nombre_estudiante')
                apellido_estudiante = item.get('apellido_estudiante')
                nombre_padre = item.get('nombre_padre')
                id_padre = item.get('id_padre')

                # Verificar que se hayan proporcionado los datos requeridos
                if not (nombre_estudiante and apellido_estudiante and nombre_padre and id_padre):
                    resultados.append({
                        'error': 'Faltan datos obligatorios en uno de los objetos',
                        'data': item
                    })
                    continue

                verificar_monto()

                # Verificar estudiante
                resultado_estudiante = verificar_estudiante(nombre_estudiante, apellido_estudiante)

                # Verificar padre
                resultado_padre = verificar_padre(id_padre, nombre_padre, nombre_estudiante)

                if resultado_estudiante['existe'] and resultado_padre['existe']:
                    resultados.append({"Pago Correcto": [resultado_estudiante, resultado_padre]})
                else:
                    resultados.append({"Pago Incorrecto": [resultado_estudiante, resultado_padre]})

            return JsonResponse({'resultados': resultados})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    


@csrf_exempt
def asociar(request):
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

            # Iterar sobre cada objeto en la lista
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

                # Asociar el estudiante con el curso
                resultado_asociacion = asociar_estudiante_curso(codigo_estudiante, codigo_curso)

                # Comprobar si la asociación fue exitosa
                if resultado_asociacion['exito']:
                    resultados.append({"Asociación Realizada": resultado_asociacion})
                else:
                    resultados.append({"Error en la Asociación": resultado_asociacion})

            return JsonResponse({'resultados': resultados})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    

def calcular_matricula (request):
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

            # Iterar sobre cada objeto en la lista
            for item in data:
                # Extraer los datos del estudiante y del curso
                codigo_estudiante = item.get('codigo_estudiante')
               
                # Verificar que se hayan proporcionado los datos requeridos
                if not (codigo_estudiante ):
                    resultados.append({
                        'error': 'Faltan datos obligatorios en uno de los objetos',
                        'data': item
                    })
                    continue

                # Asociar el estudiante con el curso
                resultados.append(matricula(codigo_estudiante))
            return JsonResponse({'resultados': resultados})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
