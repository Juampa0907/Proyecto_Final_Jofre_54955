from django.shortcuts import render, redirect, get_object_or_404
from Inicio.forms import *
from Inicio.models import *
from django.http import *
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from Usuario.forms import *
from django.db import IntegrityError


def inicio(request):
    return render(request, 'inicio.html')




def buscar_recomendacion(request):
    if request.GET.get('videojuego'):
        videojuego_busqueda = request.GET.get('videojuego')
        resultados = Recomendacion.objects.filter(videojuego__nombre__icontains=videojuego_busqueda)
        return render(request, 'resultados_busqueda_recomendacion.html', {"resultados": resultados, "videojuego_busqueda": videojuego_busqueda})
    else:
        return render(request, 'resultados_busqueda_recomendacion.html')


class VideojuegoListView(ListView):
    model = Videojuego
    template_name = 'ultimos_videojuegos.html'  
    context_object_name = 'objetos'  
    paginate_by = 3
    

class RecomndacionListView(ListView):
    model = Recomendacion
    template_name = 'ultimas_recomendaciones.html'  
    context_object_name = 'recomendaciones' 
    ordering = ['-fecha']
    paginate_by = 3

class RecomendacionDetailView(DetailView):
    model = Recomendacion
    template_name = 'recomendacion_detalle.html' 
    context_object_name = 'recomendacion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        return context

@login_required
def agregar_comentario(request, recomendacion_id):
    recomendacion = Recomendacion.objects.get(id=recomendacion_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.recomendacion = recomendacion
            comentario.save()
            return redirect('recomendacion_detalle', pk=recomendacion_id)
    else:
        form = ComentarioForm()

    return render(request, 'agregar_comentario.html', {'form': form, 'recomendacion': recomendacion})

@login_required
def editar_recomendacion(request, recomendacion_id):
    recomendacion = get_object_or_404(Recomendacion, id=recomendacion_id)
    
    
    if recomendacion.usuario != request.user:
        return HttpResponseForbidden("No tienes permiso para editar esta recomendación.")

    if request.method == 'POST':
        form = RecomendacionForm(request.POST, instance=recomendacion)
        if form.is_valid():
            form.save()
            return redirect('ultimas_recomendaciones')
    else:
        form = RecomendacionForm(instance=recomendacion)

    return render(request, 'editar_recomendacion.html', {'form': form})

@login_required
def eliminar_recomendacion(request, recomendacion_id):
    recomendacion = get_object_or_404(Recomendacion, id=recomendacion_id)

    
    if recomendacion.usuario != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar esta recomendación.")

    if request.method == 'POST':
        recomendacion.delete()
        return redirect('ultimas_recomendaciones')

    return render(request, 'eliminar_recomendacion.html', {'recomendacion': recomendacion})

@login_required
def editar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    
    
    if comentario.usuario != request.user:
        return HttpResponseForbidden("No tienes permiso para editar este comentario.")

    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('recomendacion_detalle', pk=comentario.recomendacion.id)

    else:
        form = ComentarioForm(instance=comentario)

    return render(request, 'editar_comentario.html', {'form': form})

@login_required
def eliminar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)

   
    if comentario.usuario != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar este comentario.")

    if request.method == 'POST':
        comentario.delete()
        return redirect('recomendacion_detalle', pk=comentario.recomendacion.id)


    return render(request, 'eliminar_comentario.html', {'comentario': comentario})





def buscar_juego(request):
    if request.GET.get('videojuego'):
        videojuego_busqueda = request.GET.get('videojuego')
        resultados = Videojuego.objects.filter(nombre__icontains=videojuego_busqueda)
        return render(request, 'resultados_busqueda_videojuegos.html', {"resultados": resultados, "videojuego_busqueda": videojuego_busqueda})
    else:        
        return render(request, 'resultados_busqueda_videojuegos.html')



def buscar_usuario(request):
    if request.GET.get('usuario'):
        usuario_busqueda = request.GET.get('usuario')
        resultados = User.objects.filter(username__icontains=usuario_busqueda)
        return render(request, 'resultados_busqueda_usuarios.html', {"resultados": resultados, "usuario_busqueda": usuario_busqueda})
    else:        
        return render(request, 'resultados_busqueda_usuarios.html')


@login_required
def anadir_videojuego(request):
    if request.method == 'POST':
        miFormulario = VideojuegoForm(request.POST, request.FILES)
        if miFormulario.is_valid():
            try:
                miFormulario.save()
            
                return render(request, 'inicio.html')
            except IntegrityError:
                miFormulario.add_error(None, "El videojuego ya existe")
    else:
        miFormulario = VideojuegoForm()
    return render(request, 'anadir_videojuego.html', {'miFormulario':miFormulario})