from django.urls import path
from Inicio import views
from django.contrib.auth.views import *
from .views import *


urlpatterns = [
    path('', views.inicio, name='Inicio'),
    #path('ultimas_recomendaciones', views.ultimas_recomendaciones, name="ultimas_recomendaciones"),
    path('buscar_recomendaciones/', views.buscar_recomendacion, name='buscar_recomendaciones'),
    #path('ultimos-videojuegos/', views.ultimos_videojuegos, name='ultimos_videojuegos'),
    path('buscar_juego/', views.buscar_juego, name='buscar_juego'),  
    path('ultimos-videojuegos/', VideojuegoListView.as_view(), name='ultimos_videojuegos'), 
    path('Inicio/ultimas_recomendaciones/', RecomndacionListView.as_view(), name='ultimas_recomendaciones'),
    path('ultimas_recomendaciones/<int:pk>/', RecomendacionDetailView.as_view(), name='recomendacion_detalle'),
    path('agregar_comentario/<int:recomendacion_id>/', views.agregar_comentario, name='agregar_comentario'),
    path('editar_recomendacion/<int:recomendacion_id>/', views.editar_recomendacion, name='editar_recomendacion'),
    path('eliminar_recomendacion/<int:recomendacion_id>/', views.eliminar_recomendacion, name='eliminar_recomendacion'),
    path('editar_comentario/<int:comentario_id>/', views.editar_comentario, name='editar_comentario'),
    path('eliminar_comentario/<int:comentario_id>/', views.eliminar_comentario, name='eliminar_comentario'),
    path('buscar_usuarios/', views.buscar_usuario, name='buscar_usuarios'),
    path('anadir-videojuego/', views.anadir_videojuego, name='anadir_videojuego'),
   ]