from django.core.management.base import BaseCommand
from gestorUsuarios.models import Usuario

class Command(BaseCommand):
    help = 'Poblar la base de datos con usuarios de ejemplo'

    def handle(self, *args, **kwargs):
        usuarios = [
            {'nombre': 'Carlos', 'apellido': 'Pérez', 'tipo': 'AF', 'idEstudiante': 10101},
            {'nombre': 'Ana', 'apellido': 'Gómez', 'tipo': 'Profesor', 'idEstudiante': None},
            {'nombre': 'Luisa', 'apellido': 'Martínez', 'tipo': 'AF', 'idEstudiante': 10202},
        ]

        for usuario_data in usuarios:
            # Crea el usuario o lo encuentra si ya existe
            usuario, created = Usuario.objects.get_or_create(
                nombre=usuario_data['nombre'],
                apellido=usuario_data['apellido'],
                tipo=usuario_data['tipo'],
                idEstudiante=usuario_data['idEstudiante']
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Usuario {usuario.nombre} {usuario.apellido} creado."))
            else:
                self.stdout.write(self.style.WARNING(f"Usuario {usuario.nombre} {usuario.apellido} ya existe."))
