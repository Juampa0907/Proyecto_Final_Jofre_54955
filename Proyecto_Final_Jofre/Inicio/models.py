from Usuario.forms import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

generos_choices = [
    ('accion', 'Acción'),
    ('aventura', 'Aventura'),
    ('rol', 'RPG'),
    ('estrategia', 'Estrategia'),
    ('deporte', 'Deporte'),
    ('disparos', 'Disparos'),
    ('plataformas', 'Plataformas'),
    ('simulacion', 'Simulación'),
    ('puzzle', 'Puzzle'),
    ('moba', 'MOBA')
] #lo agrego para que el usuario no tenga la opcion de "inventar"
#y solo pueda elegir opciones predeterminadas

plataformas_choices = [
    ('pc', 'PC'),
    ('ps4', 'PS4'),
    ('xbox', 'Xbox'),
    ('switch', 'Nintendo Switch'),
    ('mobile', 'Dispositivos Móviles'),
]

    
class Videojuego(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ano_lanzamiento = models.IntegerField()
    genero = models.CharField(max_length=50, choices=generos_choices)
    desarrollador = models.CharField(max_length=100)
    plataforma = models.CharField(max_length=50)
    descripcion = models.TextField()
    requisitos_sistema = models.TextField()
    imagen = models.ImageField(upload_to='juegos/', blank=True, null=True)  # Campo para la imagen


    def __str__(self):
        return f"{self.nombre}"
    
    

#las foreignkeys las uso para que si se elimina el usuario que
#creó la recomendacion tambien se elimine la recomendacion
#lo mismo para con el videojuego

#ademas esto me sirve para decir que usuario crea tal recomendacion para tal videojuego



class Recomendacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    puntuacion = models.FloatField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    imagen = models.ImageField(upload_to='recomendaciones/', blank=True, null=True)  # Campo para la imagen

    def __str__(self):
        return f"Recomendacion: {self.videojuego.nombre} - Usuario: {self.usuario.username}"
    
    class Meta:
        # Definir restricción de unicidad para usuario y videojuego
       unique_together = ('usuario', 'videojuego')




class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    recomendacion = models.ForeignKey(Recomendacion, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()

    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.recomendacion}"

# Create your models here.
