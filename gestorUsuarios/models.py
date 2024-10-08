from django.db import models

class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    tipo = models.CharField(max_length=2)
    idEstudiante = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
