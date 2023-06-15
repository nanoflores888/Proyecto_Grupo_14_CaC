from django.shortcuts import render
from noticias.models import Post, Categoria

# Create your views here.
def noticias(request):

    posts=Post.objects.all()
    return render(request, "noticias/noticias.html", {"posts": posts})


def categoria(request, categoria_id):

    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request, "noticias/categoria.html", {'categoria': categoria, 
"posts": posts})






















































