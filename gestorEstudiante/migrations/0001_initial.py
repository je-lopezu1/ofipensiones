# Generated by Django 3.2.6 on 2024-10-17 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestorCursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('curso', models.ManyToManyField(related_name='estudiantes', to='gestorCursos.Curso')),
            ],
        ),
    ]
