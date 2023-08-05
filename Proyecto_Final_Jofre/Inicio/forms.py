from django import forms
from .models import *
import datetime 
from django.core.exceptions import ValidationError
class VideojuegoForm(forms.ModelForm):
    imagen = forms.ImageField(required=False)  # Campo para la imagen
    plataforma = forms.MultipleChoiceField(choices=plataformas_choices, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Videojuego
        fields = '__all__'  
        labels = {
            'nombre': 'Nombre del videojuego',
            'ano_lanzamiento': 'Año de lanzamiento',
            'genero': 'Género',
            'desarrollador': 'Desarrollador',
            'plataforma': 'Plataforma',
            'descripcion': 'Descripción',
            'requisitos_sistema': 'Requisitos del sistema',
        }

        def clean_nombre(self):
            nombre = self.cleaned_data.get('nombre')
            if nombre:
                return nombre.upper()  
            return nombre
        
        def clean_ano_lanzamiento(self):
            ano_lanzamiento = self.cleaned_data['ano_lanzamiento']
            current_year = datetime.date.today().year

            if ano_lanzamiento > current_year:
                raise forms.ValidationError("El año de lanzamiento no puede ser mayor al año actual.")
            
            return ano_lanzamiento


class RecomendacionForm(forms.ModelForm):
    imagen = forms.ImageField(required=False)  

    class Meta:
        model = Recomendacion
        fields = ('videojuego', 'comentario', 'puntuacion', 'imagen')  
        labels = {
            'videojuego': 'Videojuego',
            'comentario': 'Comentario',
            'puntuacion': 'Puntuación',
            'imagen': 'Imagen',  
        }
        widgets = {
            'usuario': forms.HiddenInput(),
        }
    def clean_puntuacion(self):
        puntuacion = self.cleaned_data.get('puntuacion')
        if not 1 <= puntuacion <= 10:
            raise ValidationError('La puntuación debe estar entre 1 y 10.')
        return puntuacion




class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'texto': 'Agregar un comentario',
        }