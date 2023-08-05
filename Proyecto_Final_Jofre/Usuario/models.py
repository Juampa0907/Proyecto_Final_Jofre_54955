from django.db import models
from django.contrib.auth.models import User


PROVINCIAS_CHOICES = [
    ('buenos_aires', 'Buenos Aires'),
    ('caba', 'Ciudad Autónoma de Buenos Aires'),
    ('catamarca', 'Catamarca'),
    ('chaco', 'Chaco'),
    ('chubut', 'Chubut'),
    ('cordoba', 'Córdoba'),
    ('corrientes', 'Corrientes'),
    ('entre_rios', 'Entre Ríos'),
    ('formosa', 'Formosa'),
    ('jujuy', 'Jujuy'),
    ('la_pampa', 'La Pampa'),
    ('la_rioja', 'La Rioja'),
    ('mendoza', 'Mendoza'),
    ('misiones', 'Misiones'),
    ('neuquen', 'Neuquén'),
    ('rio_negro', 'Río Negro'),
    ('salta', 'Salta'),
    ('san_juan', 'San Juan'),
    ('san_luis', 'San Luis'),
    ('santa_cruz', 'Santa Cruz'),
    ('santa_fe', 'Santa Fe'),
    ('santiago_del_estero', 'Santiago del Estero'),
    ('tierra_del_fuego', 'Tierra del Fuego'),
    ('tucuman', 'Tucumán'),
]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    provincia = models.CharField(max_length=50, choices=PROVINCIAS_CHOICES, default='')
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    sobre_mi = models.TextField(blank=True, null=True)  
    steam_url = models.URLField(blank=True, null=True)  
    twitter_url = models.URLField(blank=True, null=True) 
    instagram_url = models.URLField(blank=True, null=True)  

    def __str__(self):
        return f"Perfil de {self.user.username}"


# Create your models here.
