from django.db import models


class Estudiante(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)  # Campo para el nombre del estudiante
    apellido = models.CharField(max_length=100)  # Campo para el apellido del estudiante
    curso = models.CharField(max_length=100)  # Campo para el curso en el que está inscrito

    # Este método devuelve una representación en cadena de un objeto estudiante
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.curso}"
