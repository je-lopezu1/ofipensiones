import hashlib as hash

from gestorCursos.models import Curso
from gestorPersistencia.models import Hash
from django.http import JsonResponse
import random

def guardar_curso(curso):
    # Crear un nuevo curso
    curso.save()

    id = curso.id
    nombre = curso.nombre
    codigo = curso.codigo

    informacion = nombre+codigo

    # Crear un hash del curso
    curso_hash = hash.sha256(informacion.encode()).hexdigest()

    # Guardar Hash
    curso_hash = Hash(id=id, hash=curso_hash)
    curso_hash.save()
    
    # Devolver un mensaje de éxito
    return curso

def revision_hash():
    # Obtener todos los cursos
    cursos = Curso.objects.all()

    # Crear un diccionario para almacenar los hashes
    iguales = True
    i = 0

    while iguales and i < len(cursos):
        # Obtener el curso
        curso = cursos[i]

        # Obtener el hash del curso
        hash_modelo = Hash.objects.get(id=curso.id)

        # Crear un hash del curso
        informacion = curso.nombre+curso.codigo
        curso_hash = hash.sha256(informacion.encode()).hexdigest()

        # Verificar si el hash es igual
        iguales = curso_hash == hash_modelo.hash

        i += 1

    # Devolver el diccionario con los hashes
    return iguales

def pruebas_seguridad():
    cantidad_cursos = len(Curso.objects.all())
    id1 = random.randint(1, cantidad_cursos+1)
    nombre = "Curso de prueba"
    modificar_curso(id1, nombre)

    respuesta = revision_hash()

    texto =""
    if respuesta:
        texto = "Los hashes son iguales"
    else:
        texto = "Los hashes no son iguales"

    eliminar_curso(id1)
    
    # Eliminar hash
    hash_modelo = Hash.objects.get(id=id1)
    hash_modelo.delete()

    # Retorna el texto como un JSON
    return JsonResponse({'resultado': texto})

def modificar_curso(id, nombre):
    # Obtener el curso
    curso = Curso.objects.get(id=id)

    # Modificar el nombre del curso
    curso.nombre = nombre

    # Guardar el curso
    curso.save()

    # Devolver un mensaje de éxito
    return curso

def eliminar_curso(id):
    # Obtener el curso
    curso = Curso.objects.get(id=id)

    # Eliminar el curso
    curso.delete()

    # Devolver un mensaje de éxito
    return curso

# Haz una funcion que elimine todos los cursos y hashes
def eliminar_cursos():
    # Obtener todos los cursos
    cursos = Curso.objects.all()

    # Eliminar cada curso
    for curso in cursos:
        curso.delete()

    # Obtener todos los hashes
    hashes = Hash.objects.all()

    # Eliminar cada hash
    for h in hashes:
        h.delete()

    # Devolver un mensaje de éxito
    return JsonResponse({'resultado': 'Todos los cursos y hashes han sido eliminados.'})
