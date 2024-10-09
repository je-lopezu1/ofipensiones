from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from gestorEstudiante.views import verificar_estudiante as verificar_estudiante
from gestorUsuarios.views import verificar_padre as verificar_padre
from gestorFinanciero.views import verificar_monto as verificar_monto

csrf_exempt  
def verificar(request):
    
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
                     resultados.append({"Pago Correcto":[resultado_estudiante,resultado_padre]})
                else:
                    resultados.append({"Pago Incorrecto":[resultado_estudiante,resultado_padre]})
           

            return JsonResponse({'resultados': resultados})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)

