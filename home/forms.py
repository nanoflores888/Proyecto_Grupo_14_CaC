from django import forms
from django.forms import ModelForm, TextInput, EmailInput, NumberInput
from .models import Contacto 
    
class UserInfoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'apellido', 'telefono', 'email', 'mensaje']
        widgets = {
            'nombre': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Nombre'
                }),
            'apellido': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 600px;',
                'placeholder': 'Apellido'
                }),
            'telefono': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Telefono'
                }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Email'
                }),
            'mensaje': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px; max-height: 600px;',
                'placeholder': 'Mensaje'
                }),
        }