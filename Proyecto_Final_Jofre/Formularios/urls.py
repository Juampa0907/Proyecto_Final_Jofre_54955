from django.urls import path, include
from django.contrib.auth.views import *
from Formularios import views

urlpatterns = [
    path('login', views.login_request, name='Login'),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name= 'logout.html'), name='Logout'),
    path('crear-recomendacion/', views.crear_recomendacion, name='crear_recomendacion'),
    #path('anadir-videojuego/', views.anadir_videojuego, name='anadir_videojuego'),
    
]
