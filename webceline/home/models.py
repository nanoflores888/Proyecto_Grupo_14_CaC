from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email = models.EmailField()
    mensaje = models.CharField(max_length=250)
    
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.telefono} - {self.email} - {self.mensaje}"