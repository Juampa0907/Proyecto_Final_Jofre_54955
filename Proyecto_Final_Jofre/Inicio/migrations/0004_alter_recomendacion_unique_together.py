# Generated by Django 4.2.2 on 2023-08-03 02:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Inicio', '0003_videojuego_imagen'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='recomendacion',
            unique_together={('usuario', 'videojuego')},
        ),
    ]
