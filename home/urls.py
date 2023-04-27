from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.home, name="home"),
    path('home/sobre_mi/', views.sobre_mi, name="sobre_mi"),
    path('home/resumen/', views.resumen, name="resumen"),
    path('home/proyecto_F4/', views.proyecto_F4, name="proyecto_F4"),
    path('home/galeria/', views.galeria, name="galeria"),
    path('contacto/', views.contacto, name="contacto"),
]