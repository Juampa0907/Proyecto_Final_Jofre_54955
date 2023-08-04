# Generated by Django 4.2.2 on 2023-08-03 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='telefono',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='provincia',
            field=models.CharField(choices=[('buenos_aires', 'Buenos Aires'), ('caba', 'Ciudad Autónoma de Buenos Aires'), ('catamarca', 'Catamarca'), ('chaco', 'Chaco'), ('chubut', 'Chubut'), ('cordoba', 'Córdoba'), ('corrientes', 'Corrientes'), ('entre_rios', 'Entre Ríos'), ('formosa', 'Formosa'), ('jujuy', 'Jujuy'), ('la_pampa', 'La Pampa'), ('la_rioja', 'La Rioja'), ('mendoza', 'Mendoza'), ('misiones', 'Misiones'), ('neuquen', 'Neuquén'), ('rio_negro', 'Río Negro'), ('salta', 'Salta'), ('san_juan', 'San Juan'), ('san_luis', 'San Luis'), ('santa_cruz', 'Santa Cruz'), ('santa_fe', 'Santa Fe'), ('santiago_del_estero', 'Santiago del Estero'), ('tierra_del_fuego', 'Tierra del Fuego'), ('tucuman', 'Tucumán')], default='', max_length=50),
        ),
    ]
