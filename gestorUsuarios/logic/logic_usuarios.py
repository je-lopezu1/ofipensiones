from gestorUsuarios.models import Usuario
from gestorEstudiante.models import Estudiante
from django.core.exceptions import ObjectDoesNotExist

# Verificar que la persona que realizo el pago si existe y es un Acudiente financiero (AF)  
def verificar_af(id_af, nombre, nombre_estudiante):
    try:
        usuario = Usuario.objects.get(id=id_af)

        nom_estudiante = Estudiante.objects.get(id=usuario.idEstudiante).nombre

        if usuario.nombre == nombre and usuario.tipo == 'AF' and nombre_estudiante == nom_estudiante:
            return {'existe': True, 'mensaje': 'El nombre coincide con el ID.'}
        else:
            return {'existe': False, 'mensaje': 'El nombre no coincide con el ID.'}
    except ObjectDoesNotExist:
        return {'existe': False, 'mensaje': 'Usuario no encontrado.'}
    
