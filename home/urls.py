from django.urls import path, include
from . import views
from home.admin import web_admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', web_admin.urls),
    path('home/sobre_mi/', views.sobre_mi, name="sobre_mi"),
    path('home/resumen/', views.resumen, name="resumen"),
    path('home/proyecto_F4/', views.proyecto_F4, name="proyecto_F4"),
    path('home/noticias/', views.noticias, name="noticias"),
    #path('home/noticias/', views.listar_publicaciones, name='listar_publicaciones'),
    path('home/nueva_noticia/', views.nueva_noticia, name="nueva_noticia"),
    path('home/galeria/', views.galeria, name="galeria"),
    path('home/contacto/', views.contacto, name="contacto"),
    
    #autenticacion
    path('accounts/register', views.registro, name='registro'),
    
    #por defecto de django    
    path('accounts/login/', auth_views.LoginView.as_view(
            template_name='home/login.html',
        )),
    path('accounts/logout/',
         views.EditLogoutView.as_view(), name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(success_url="/"), name='password_change'), 
    path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)