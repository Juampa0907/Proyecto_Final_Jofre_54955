from django.contrib.auth.forms import *
from django.contrib.auth import *
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Email',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = []  # No se necesitan campos adicionales, ya que los campos de contraseña están en el formulario base
        labels = {
            'old_password': 'Contraseña actual',
            'new_password1': 'Nueva contraseña',
            'new_password2': 'Repetir nueva contraseña',
        }

class UserProfileForm(forms.ModelForm):
    imagen = forms.ImageField(label="Imagen de perfil", required=False)
    eliminar_imagen = forms.BooleanField(label="Eliminar imagen de perfil", required=False)

    class Meta:
        model = UserProfile
        fields = ['provincia', 'sobre_mi', 'steam_url', 'twitter_url', 'instagram_url']

        labels = {
            'provincia': 'Provincia',
            'sobre_mi': 'Sobre Mí',
            'steam_url': 'Enlace a Steam',
            'twitter_url': 'Enlace a Twitter',
            'instagram_url': 'Enlace a Instagram',
        }

        widgets = {
            'sobre_mi': forms.Textarea(attrs={'rows': 3}),
        }


