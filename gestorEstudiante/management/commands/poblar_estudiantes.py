from django.core.management.base import BaseCommand
from gestorEstudiante.models import Estudiante

class Command(BaseCommand):
    help = 'Popula la base de datos con usuarios de prueba'

    def handle(self, *args, **kwargs):
        # Crear usuarios de prueba
        estudiantes = [
            {'codigo': '202111348','nombre': 'Juan', 'apellido': 'Perez'},
            {'codigo': '202421349','nombre': 'Manuela', 'apellido': 'Martinez'},
            {'codigo': '201921359','nombre': 'Pedro', 'apellido': 'Martinez'}
        ]
        
        for estudiante in estudiantes:
            Estudiante.objects.create(
                codigo=estudiante['codigo'], 
                nombre=estudiante['nombre'], 
                apellido=estudiante['apellido'], 
               
            )
            self.stdout.write(self.style.SUCCESS(f"Estudiante {estudiante['nombre']} {estudiante['apellido']} creado"))

        self.stdout.write(self.style.SUCCESS('Estudiantes de prueba creados correctamente'))
