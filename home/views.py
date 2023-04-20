from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import UserInfoForm
from django.contrib import messages
from .forms import UserInfoForm

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

#def contacto(request):
    if request.method == 'POST':
        contacto_form = UserInfoForm(request.POST)
        if contacto_form.is_valid():
            messages.info(request, "Info Importante")
    else:
        contacto_form = UserInfoForm()
    return render(request, "home/contacto.html", {'contacto_form': contacto_form})

def contacto(request):
    return render(request, "home/contacto.html", {'form': UserInfoForm,})