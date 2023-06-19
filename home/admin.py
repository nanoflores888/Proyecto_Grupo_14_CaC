from django.contrib import admin
from home.models import *

# Register your models here.

class Admin14Site(admin.AdminSite):
    site_header = 'Administracion Grupo 14'
    site_title = 'Administracion Grupo 14'
    index_title = 'Administracion Web'
    
class ContactoEdit(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'mensaje',)
    list_editable = ('mensaje',)
    search_fields = ('apellido', 'nombre')

class RolesInline(admin.TabularInline):
    model = Persona_rol
    
class RolesAdmin(admin.ModelAdmin):
    inlines = [
        RolesInline,
    ]    

web_admin = Admin14Site(name='admin14')
web_admin.register(Contacto, ContactoEdit)
web_admin.register(Persona, RolesAdmin)
web_admin.register(Publicacion)
web_admin.register(Comentario)
web_admin.register(Persona_rol)
web_admin.register(Rol)
web_admin.register(User)



