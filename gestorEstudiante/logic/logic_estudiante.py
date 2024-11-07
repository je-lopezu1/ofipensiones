import random
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from gestorCursos.models import Curso
from gestorEstudiante.models import Estudiante
from django.core.exceptions import ObjectDoesNotExist

# Verificar que el estudiante exista
def verificar(nombre, apellido):
    try:
        estudiante = Estudiante.objects.get(nombre=nombre, apellido=apellido)

        if estudiante:
            return {'existe': True, 'mensaje': 'El estudiante es correcto.'}
       
    except ObjectDoesNotExist:
        return {'existe': False, 'mensaje': 'Estudiante NO es correcto.'}
    


def asociar_estudiante_curso(codigo_estudiante, codigo_curso):
    try:
        # Buscar el curso y el estudiante por sus códigos
        curso = get_object_or_404(Curso, codigo=codigo_curso)
        estudiante = get_object_or_404(Estudiante, codigo=codigo_estudiante)

        # Asociar el curso al estudiante
        estudiante.cursos.add(curso)

        # Devolver un mensaje de éxito
        return {'exito': True, 'mensaje': 'Curso asociado correctamente'}

    except Exception as e:
        # Manejar cualquier error que ocurra
        return {'exito': False, 'mensaje': f'Error al asociar el curso: {str(e)}'}
    
#Disponibilidad 
    
def nodo_respuesta(request):
    # Simular respuesta correcta o incorrecta
    resultado = "OK" if random.choice([True, False]) else "ERROR"
    return JsonResponse({"resultado": resultado})
    