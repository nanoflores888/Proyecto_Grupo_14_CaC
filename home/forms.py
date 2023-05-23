from django import forms
from .models import Contacto
from .models import Publicacion
from django.forms import ValidationError
import re

def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                            code='Invalid',
                            params={'valor':value})

def validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido')
    return value

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': "form-control",
                'id': 'nombre',
                'style': 'max-width: 600px;',
                'placeholder': 'Nombre',
                'maxlength': '50',
                'required': True,
                'validators': (solo_caracteres,),
                }),
            'apellido': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Apellido',
                'maxlength': '50',
                'required': True,
                'validators': (solo_caracteres,),
                }),
            'telefono': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Telefono',
                'maxlength': '50',
                'required': True
                }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Email'
                }),
            'mensaje': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 600px; max-height: 600px;',
                'placeholder': 'Mensaje',
                'maxlength': '1000',
                'required': True
                }),
        }

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido']
        widgets = {
                'titulo': forms.TextInput(attrs={
                    'class': "form-control",
                    'id': 'titulo',
                    'style': 'max-width: 600px;',
                    'placeholder': 'titulo',
                    'maxlength': '150',
                    'required': True,
                    'validators': (solo_caracteres,),
                    }),
                'contenido': forms.TextInput(attrs={
                    'class': "form-control",
                    'style': 'max-width: 800px; max-height: 800px;',
                    'placeholder': 'contenido',
                    'maxlength': '2500',
                    'required': True
                    }),
            }
