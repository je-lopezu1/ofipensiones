from django.shortcuts import render

from gestorCursos.logic.logic_curso import crear_curso


# Create your views here.
def crearCurso(codigo, nombre):
    # Crear un nuevo curso
    curso = crear_curso(codigo, nombre)

    # Devolver un mensaje de éxito
    return curso