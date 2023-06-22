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

<<<<<<< HEAD
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'display_topics']
    list_filter = ['topic']

    def display_topics(self, obj):
        topics = ", ".join(str(topic) for topic in obj.topic.all())
        return topics

    display_topics.short_description = 'Topics'
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'autor', 'texto', 'display_topics']
    list_filter = ['topic']

    def display_topics(self, obj):
        topics = ", ".join(str(topic) for topic in obj.topic.all())
        return topics

    display_topics.short_description = 'Topics'
=======
class RolesInline(admin.TabularInline):
    model = Persona_rol

class RolesAdmin(admin.ModelAdmin):
    inlines = [
        RolesInline,
    ]
>>>>>>> 4ea3cbccfd2da0339a57df5cdcfcff6f63a48791

web_admin = Admin14Site(name='admin14')
web_admin.register(Contacto, ContactoEdit)
web_admin.register(User)
<<<<<<< HEAD
web_admin.register(Post, PostAdmin)
web_admin.register(Comment, CommentAdmin)
=======
web_admin.register(Post)
web_admin.register(Comment)
>>>>>>> 4ea3cbccfd2da0339a57df5cdcfcff6f63a48791
web_admin.register(Topic)