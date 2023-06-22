from django.contrib.auth.models import User
from django.db import models

STATUS = (
    (0, "Borrador"),
    (1, "Publicar"),
    (2, "Archivar"),
)

class Topic(models.Model):
    topic = models.CharField(max_length=100, verbose_name='TOPIC', null=False, default='Opinion')

    def __str__(self):
        return self.topic

    class Meta:
        db_table = 'blog_topic'

# Crear los valores por defecto
#default_topics = ['Opinion', 'Consejo', 'Carrera', 'Clasificacion']

# Insertar los valores por defecto en la base de datos
#for topic in default_topics:
#    Topic.objects.get_or_create(topic=topic)

class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    contenido = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    imagen = models.ImageField(
        upload_to="post",
        default="../media/post/no-image.jpg",
    )
    autor = models.ForeignKey(
        User,
        related_name="blog_posts",
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    topic = models.ManyToManyField(Topic, verbose_name="TOPIC")


    def __str__(self):
        return self.titulo


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE
    )
    autor = models.ForeignKey(
        User,
        related_name="comments",
        on_delete=models.CASCADE,
    )
    texto = models.TextField()
    approved_comment = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    topic = models.ManyToManyField(Topic, verbose_name="TOPIC")

    def __str__(self):
        return self.texto
