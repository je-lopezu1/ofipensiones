from django.core.management.base import BaseCommand
from gestorEstudiante.models import Estudiante

class Command(BaseCommand):
    help = 'Popula la base de datos con usuarios de prueba'

    def handle(self, *args, **kwargs):
        # Crear usuarios de prueba
        estudiantes = [
            {'nombre': 'Juan', 'apellido': 'Perez', 'curso': 'Octavo'},
            {'nombre': 'Ana', 'apellido': 'Gomez', 'curso': 'Noveno'},
            {'nombre': 'Pedro', 'apellido': 'Martinez', 'curso': 'Primero'}
        ]
        
        for estudiante in estudiantes:
            Estudiante.objects.create(
                nombre=estudiante['nombre'], 
                apellido=estudiante['apellido'], 
                curso=estudiante['curso']
            )
            self.stdout.write(self.style.SUCCESS(f"Estudiante {estudiante['nombre']} {estudiante['apellido']} creado"))

        self.stdout.write(self.style.SUCCESS('Estudiantes de prueba creados correctamente'))
