from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import UserInfoForm
from django.contrib import messages
from .forms import UserInfoForm

def home(request):
        return render(request, "home/index.html")
    
def escuela(request):
    return render(request, "home/escuela.html")

def prensa(request):
    return render(request, "home/prensa.html")

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