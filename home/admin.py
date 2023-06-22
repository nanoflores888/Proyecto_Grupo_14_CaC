from django.contrib import admin
from blog.models import *
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

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('topic',)
    list_display = ['titulo', 'display_topics']
    list_filter = ['topic']

    def display_topics(self, obj):
        topics = ", ".join(str(topic) for topic in obj.topic.all())
        return topics

    display_topics.short_description = 'Topics'
    
class CommentAdmin(admin.ModelAdmin):
    filter_horizontal = ('topic',)
    list_display = ['post', 'autor', 'texto', 'display_topics']
    list_filter = ['topic']

    def display_topics(self, obj):
        topics = ", ".join(str(topic) for topic in obj.topic.all())
        return topics

    display_topics.short_description = 'Topics'

web_admin = Admin14Site(name='admin14')
web_admin.register(Contacto, ContactoEdit)
#web_admin.register(Persona, RolesAdmin)
#web_admin.register(Publicacion)
#web_admin.register(Comentario)
#web_admin.register(Persona_rol)
#web_admin.register(Rol)
web_admin.register(User)
web_admin.register(Post, PostAdmin)
web_admin.register(Comment, CommentAdmin)
web_admin.register(Topic)