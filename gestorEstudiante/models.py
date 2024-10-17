from django.db import models

from gestorCursos.models import Curso


class Estudiante(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)  # Campo para el nombre del estudiante
    apellido = models.CharField(max_length=100)  # Campo para el apellido del estudiante
    cursos = models.ManyToManyField(Curso, related_name='estudiantes') 

    # Este método devuelve una representación en cadena de un objeto estudiante
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.curso}"
