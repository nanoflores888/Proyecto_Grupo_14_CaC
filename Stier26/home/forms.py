from django import forms
from .models import Contacto

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'apellido', 'telefono', 'email', 'mensaje']
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
            'mensaje': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 600px; height: 300px;',
                'placeholder': 'Mensaje'
                }),
        }
        