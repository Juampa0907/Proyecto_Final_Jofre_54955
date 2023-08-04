# Generated by Django 4.2.2 on 2023-07-31 22:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Videojuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ano_lanzamiento', models.IntegerField()),
                ('genero', models.CharField(choices=[('accion', 'Acción'), ('aventura', 'Aventura'), ('rol', 'RPG'), ('estrategia', 'Estrategia'), ('deporte', 'Deporte'), ('disparos', 'Disparos'), ('plataformas', 'Plataformas'), ('simulacion', 'Simulación'), ('puzzle', 'Puzzle')], max_length=50)),
                ('desarrollador', models.CharField(max_length=100)),
                ('plataforma', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('requisitos_sistema', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recomendacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('puntuacion', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('videojuego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inicio.videojuego')),
            ],
        ),
    ]
