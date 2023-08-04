from django.urls import path
from django.contrib.auth.views import *
from Usuario import views

urlpatterns = [
    path("",views.inicio_usuario, name="inicio_usuario"),
    path('actualizar_perfil/', views.actualizar_perfil, name='actualizar_perfil'),
    path('perfil_usuario/<int:usuario_id>/', views.perfil_usuario, name='perfil_usuario'),
    path('editar_usuario/', views.editar_usuario, name='editar_usuario'),
    path('cambiar_contraseña/', views.cambiar_contraseña, name='cambiar_contraseña'),

    
]