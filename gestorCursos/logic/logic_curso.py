from gestorCursos.models import Curso
from gestorPersistencia.logic.logic_persistencia import guardar_curso

def crear_curso(codigo, nombre):
    # Crear un nuevo curso
    curso = Curso(codigo=codigo, nombre=nombre)

    # Guardar el curso
    guardar_curso(curso)

    # Devolver un mensaje de éxito
    return curso