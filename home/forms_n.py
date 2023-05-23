from django import forms
from .models import Noticias

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = ['nombre', 'apellido', 'telefono', 'email','titulo', 'contenido']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Nombre'
                }),
            'apellido': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Apellido'
                }),
            'telefono': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Telefono'
                }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Email'
                }),
            'titulo': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 600px; max-height: 600px;',
                'placeholder': 'Título'
                }),
            'contenido': forms.Textarea(attrs={
            'class': "form-control",
            'style': 'max-width: 600px; max-height: 600px;',
            'placeholder': 'Contenido'}),
        }