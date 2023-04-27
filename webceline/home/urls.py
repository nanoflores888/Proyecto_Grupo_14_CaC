from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.home, name="home"),
    path('home/escuela/', views.escuela, name="escuela"),
    path('home/prensa/', views.prensa, name="prensa"),
    path('contacto/', views.contacto, name="contacto"),
]