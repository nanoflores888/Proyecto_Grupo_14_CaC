from django import forms
from .models import Contacto, Publicacion, User
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm

def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('No puede contener valores numéricos.',
                            code='Invalid',
                            params={'valor':value})

class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(
        validators=[solo_caracteres],
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': 'id_nombre',
            'style': 'max-width: 600px;',
            'placeholder': 'Nombre',
            'required': True,
        })
    )

    apellido = forms.CharField(
        validators=[solo_caracteres],
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': 'id_apellido',
            'style': 'max-width: 600px;',
            'placeholder': 'Apellido',
            'required': True,
        })
    )

    telefono = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': 'id_telefono',
            'style': 'max-width: 600px;',
            'placeholder': 'Telefono',
            'required': False,
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': "form-control",
            'id': 'id_email',
            'style': 'max-width: 600px;',
            'placeholder': 'Email',
            'required': True,
        })
    )

    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': "form-control",
            'id': 'id_mensaje',
            'style': 'max-width: 600px; max-height: 600px;',
            'placeholder': 'Mensaje',
            'required': True,
        })
    )

    class Meta:
        model = Contacto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name in self.errors:
                field.widget.attrs['class'] += ' is-invalid'

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

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email' , 'password1', 'password2']