# Generated by Django 4.1 on 2022-08-22 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=25)),
                ('Apellido', models.CharField(max_length=30)),
                ('Año_de_nacimiento', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Fecha_actual', models.DateField()),
            ],
        ),
    ]
