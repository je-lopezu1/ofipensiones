from django.core.management.base import BaseCommand
from gestorEstudiante.models import Estudiante

class Command(BaseCommand):
    help = 'Elimina todos los estudiantes de la base de datos'

    def handle(self, *args, **kwargs):
        Estudiante.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Todos los estudiantes han sido eliminados'))
