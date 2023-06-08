from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.db import models
from django.core.validators import MinLengthValidator

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

# Modelo de la clase Persona
class Persona(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    nombre = models.CharField(max_length=100, verbose_name="NOMBRE")
    apellido = models.CharField(max_length=100, verbose_name="APELLIDO")
    email = models.EmailField(null=False, verbose_name="EMAIL")
    contraseña = models.CharField(max_length=128, null=False, verbose_name="CONTRASEÑA")
    estado_activo = models.BooleanField(default=1)

    class Meta:
        db_table = 'PERSONA'

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.apellido} - {self.email} - {self.contraseña}"

    def set_password(self, password):
        self.contraseña = make_password(password)

    def check_password(self, raw_password):
        return authenticate(raw_password=raw_password, password=self.contraseña) is not None

    def soft_delete(self):
        self.baja=True
        super().save()

    def restore(self):
        self.baja=False
        super().save()
    
    def set_roles(self, roles):
        for role in roles:
            rol, _ = Rol.objects.get_or_create(detalle_rol=role)
            Persona_rol.objects.create(id_persona=self, id_rol=rol)

# Modelo de la clase ROL
class Rol(models.Model):
    ROLES = [
        (1,'Admin'),
        (2,'Aprobador'),
        (3, 'Autor'),
    ]
    id = models.AutoField(primary_key=True, verbose_name="ID")
    detalle_rol = models.IntegerField(choices=ROLES ,default= 3, verbose_name="DETALLE_ROL")
    fecha_creacion = models.DateField(auto_now= True, null=False, verbose_name="FECHA_CREACION")
    fecha_modificacion = models.DateField(auto_now=True, null=True, verbose_name="FECHA_MODIFICACION")

    class Meta:
        db_table = 'ROL'

    def __str__(self):
        return self.get_detalle_rol_display()

    def get_detalle_rol_display(self):
        return dict(self.ROLES).get(self.detalle_rol)


# Modelo de la clase Persona_rol
class Persona_rol(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name="ID_ROL", null=False)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, verbose_name="ID_PERSONA", null=False)
    fecha_creacion = models.DateField(auto_now= True, null=False, verbose_name="FECHA_CREACION")
    fecha_modificacion = models.DateField(auto_now=True, null=True, verbose_name="FECHA_MODIFICACION")

    class Meta:
        db_table = 'PERSONA_ROL'

    def __str__(self):
        return f"{self.id_persona} - {self.id_rol}"

# Modelo de la clase Publicacion
class Publicacion(models.Model):
    ESTADO = [
        (1,'Pendiente'),
        (2,'Aprobada'),
    ]
    id = models.AutoField(primary_key=True, verbose_name="ID")
    titulo = models.CharField(max_length=100, null=False, verbose_name="TITULO")
    contenido = models.TextField(max_length=5000, null=False, verbose_name="CONTENIDO")
    estado = models.CharField(choices=ESTADO ,default= 1, max_length=20, null=False, verbose_name="ESTADO")
    fecha_creacion = models.DateField(auto_now= True, null=False, verbose_name="FECHA_CREACION")
    fecha_modificacion = models.DateField(auto_now=True, null=True, verbose_name="FECHA_MODIFICACION")
    #id_persona_rol = models.ForeignKey(Persona_rol, on_delete=models.CASCADE, null=False, verbose_name="ID_PERSONA_ROL")

    class Meta:
        db_table = 'PUBLICACION'

    def __str__(self):
        return f"{self.titulo} - {self.contenido}"

    def restore(self):
        self.baja=False
        super().save()

# Modelo de la clase Comentario
class Comentario(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    contenido = models.TextField(max_length=500, null=False, verbose_name="CONTENIDO")
    fecha_creacion = models.DateTimeField(auto_now= True, verbose_name="FECHA_CREACION")
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True, verbose_name="FECHA_MODIFICACION")
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, verbose_name="ID_PERSONA")
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, verbose_name="ID_PUBLICACION")

    class Meta:
        db_table = 'COMENTARIO'

    def __str__(self):
        return f"{self.id} - {self.contenido}"