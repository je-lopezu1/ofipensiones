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
    