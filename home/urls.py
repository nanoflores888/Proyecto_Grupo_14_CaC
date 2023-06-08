from django.urls import path
from . import views
from . import views
from django.urls import re_path
from home.admin import web_admin

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', web_admin.urls),
    path('home/sobre_mi/', views.sobre_mi, name="sobre_mi"),
    path('home/resumen/', views.resumen, name="resumen"),
    path('home/proyecto_F4/', views.proyecto_F4, name="proyecto_F4"),
    path('home/noticias/', views.noticias, name="noticias"),
    #path('home/noticias/', views.listar_publicaciones, name='listar_publicaciones'),
    path('home/nueva_noticia/', views.nueva_noticia, name="nueva_noticia"),
    path('home/galeria/', views.galeria, name="galeria"),
    path('home/contacto/', views.contacto, name="contacto"),
]