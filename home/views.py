from django.shortcuts import redirect, render
from .forms import ContactoForm
from .forms import PublicacionForm
from .models import Publicacion
from django.contrib import messages

def home(request):
    return render(request, "home/index.html")

def sobre_mi(request):
    return render(request, "home/sobre_mi.html")

def resumen(request):
    return render(request, "home/resumen.html")

def proyecto_F4(request):
    return render(request, "home/proyecto_F4.html")

def galeria(request):
    return render(request, "home/galeria.html")

def noticias(request):
    return render(request, "home/noticias.html")


'''------- CRUD DE CONTACTO -------'''

def contacto(request):
    if request.method == "POST":
        contact_form = ContactoForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Mensaje enviado correctamente.')
            return render(request, "home/contacto.html", {'contact_form': contact_form})
    else:
        contact_form = ContactoForm()
    return render(request, "home/contacto.html", {'contact_form': contact_form})


'''------- CRUD DE PUBLICACIONES -------'''

def nueva_noticia(request):
    if(request.method == 'POST'):
        publication_form = PublicacionForm(request.POST)
        if publication_form.is_valid():
            publication_form.save()
            messages.success(request, 'Mensaje enviado correctamente.')
            return render(request, "home/nueva_noticia.html", {'publication_form': publication_form})
    else:
            publication_form = PublicacionForm()
    return render(request, "home/nueva_noticia.html", {'publication_form': publication_form})

def listar_publicaciones(request):
    #queryset
    publicaciones = Publicacion.objects.all()
    return render(request,'home/noticias.html',{'publication_form': publicaciones})