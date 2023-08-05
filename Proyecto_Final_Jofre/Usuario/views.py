from django.shortcuts import render, redirect, get_object_or_404
from Usuario.forms import *
from django.contrib.auth.decorators import *
from Usuario.models import UserProfile
from Inicio.models import *
from django.contrib import messages

@login_required
def inicio_usuario(request):
    return render(request, "inicio_usuario.html")


@login_required
def actualizar_perfil(request):
    
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    reseñas_usuario = Recomendacion.objects.filter(usuario=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            if 'imagen' in request.FILES:
                profile.imagen = request.FILES['imagen']
            if profile_form.cleaned_data['eliminar_imagen']:
                profile.imagen = None  
            profile.save()
            return redirect('inicio_usuario')
    else:
        profile_form = UserProfileForm(instance=profile)

    return render(request, 'actualizar_perfil.html', {'profile_form': profile_form, 'userprofile': profile,'reseñas_usuario': reseñas_usuario})


def perfil_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)
    return render(request, 'perfil_usuario.html', {'usuario': usuario})

@login_required
def editar_usuario(request):
    user = request.user
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            
            return redirect('editar_usuario')
    else:
        form = UserForm(instance=user)
    return render(request, 'editar_usuario.html', {'form': form})





@login_required
def cambiar_contraseña(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contraseña cambiada exitosamente.')
            return redirect('editar_usuario')
    else:
        form = ChangePasswordForm(user=request.user)
    return render(request, 'cambiar_contraseña.html', {'form': form})
