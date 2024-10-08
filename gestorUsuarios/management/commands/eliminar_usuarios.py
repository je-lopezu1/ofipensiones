from django.core.management.base import BaseCommand
from gestorUsuarios.models import Usuario

class Command(BaseCommand):
    help = 'Eliminar todos los usuarios de la base de datos'

    def handle(self, *args, **kwargs):
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            usuario.delete()
        self.stdout.write(self.style.SUCCESS('Usuarios eliminados.'))