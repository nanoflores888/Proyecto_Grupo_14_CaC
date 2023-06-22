from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from .forms import RegistroForm, ContactoForm

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


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Cuenta creada!')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'home/registro.html', {'form': form, 'title': 'Registro'})

class EditLogoutView(LogoutView):
    next_page = 'home'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Sesion finalizada.')
        return response