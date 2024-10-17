from django.core.management.base import BaseCommand
from gestorCursos.models import Curso

class Command(BaseCommand):
    help = 'Popula la base de datos con usuarios de prueba'

    def handle(self, *args, **kwargs):
        # Crear usuarios de prueba
        cursos = [
            {'codigo': 'ESP2021','nombre': 'Español'},
            {'codigo': 'MAT2021','nombre': 'Matemáticas'},
            {'codigo': 'FIS2021','nombre': 'Física'}]
        
        for curso in cursos:
            Curso.objects.create(
                codigo=curso['codigo'],
                nombre=curso['nombre']
            )
            self.stdout.write(self.style.SUCCESS(f"Curso {curso['codigo']} {curso['nombre']} creado"))

        self.stdout.write(self.style.SUCCESS('Cursos de prueba creados correctamente'))