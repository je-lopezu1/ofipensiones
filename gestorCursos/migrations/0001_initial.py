# Generated by Django 3.2.6 on 2024-10-16 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
    ]