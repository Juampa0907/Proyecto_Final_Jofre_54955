from django.shortcuts import render, redirect
from Usuario.forms import *
from Inicio.templates import *
from Inicio.forms import *
from django.contrib.auth.decorators import *
from Inicio.models import *
from Usuario.models import UserProfile
from Usuario.forms import *
from django.db import IntegrityError


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return render(request, 'inicio.html', {"mensaje": "Usuario Creado"})
    else:
        form = UserRegisterForm()
    return render(request, 'registro.html', {"form": form})


def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra =  form.cleaned_data.get('password')

            user= authenticate(username=usuario, password= contra)

            if user is not None:
                login(request, user)

                return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})

            else:
                return render(request, "inicio.html", {"mensaje": "Error, datos incorrectos"})
            
        else:
            return render(request, "inicio.html", {"mensaje": "Error, formulario incorrecto"})

    form=AuthenticationForm()
    #avatares=UserProfile.objects.filter(user=request.user.id)
    return render(request, "login.html", {'form':form}) #{'avatar':avatares[0].imagen.url})

@login_required
def crear_recomendacion(request):
    if request.method == 'POST':
        form = RecomendacionForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                recomendacion = form.save(commit=False)
                recomendacion.usuario = request.user
                recomendacion.save()
               
                return redirect('Inicio')  # Redirigir a la página de inicio o la que desees después de guardar la recomendación
            except IntegrityError:
                form.add_error(None, "Ya has realizado una recomendación para este videojuego.")
    else:
        form = RecomendacionForm()
    return render(request, 'crear_recomendacion.html', {'miFormulario': form})


