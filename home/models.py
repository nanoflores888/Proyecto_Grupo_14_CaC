from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email = models.EmailField()
    mensaje = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.telefono} - {self.email} - {self.mensaje}"
    

    class Noticias(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email = models.EmailField()
    titulo = models.CharField(max_length=30)
    contenido = models.CharField(max_length=2000)
    
    
    
def __str__(self):
    return f"{self.nombre} - {self.apellido} - {self.telefono} 
- {self.email} - {self.titulo} - {self.contenido}"