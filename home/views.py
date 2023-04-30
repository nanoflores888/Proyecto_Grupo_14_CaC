from django.shortcuts import redirect, render
from .forms import UserInfoForm
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

def contacto(request):
    if request.method == 'POST':
        contact_form = UserInfoForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Mensaje enviado correctamente.')
            return redirect('home/confirmacion_envio.html')
    else:
        contact_form = UserInfoForm()

    return render(request, "home/contacto.html", {'contact_form': contact_form})