# Generated by Django 5.1.1 on 2024-10-14 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apaterno', models.CharField(max_length=50, verbose_name='Apellido Paterno')),
                ('amaterno', models.CharField(max_length=50, verbose_name='Apellido Materno')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre(s)')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('fecha_ingreso', models.DateField(verbose_name='Fecha de Ingreso')),
            ],
        ),
    ]
