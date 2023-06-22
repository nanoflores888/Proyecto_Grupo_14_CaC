from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Modelo de la clase Contacto
class Contacto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="NOMBRE", null=False)
    apellido = models.CharField(max_length=50, verbose_name="APELLIDO", null=False)
    telefono = models.IntegerField(max_length=50, verbose_name="TELEFONO", null=False)
    email = models.EmailField(verbose_name="EMAIL", null=False)
    mensaje = models.CharField(max_length=1000, verbose_name="MENSAJE", validators=[MinLengthValidator(20)] ,null=False)

    class Meta:
        db_table = 'CONTACTO'

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"