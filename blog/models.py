from django.contrib.auth.models import User
from django.db import models

STATUS = (
    (0, "Borrador"),
    (1, "Publicar"),
    (2, "Archivar"),
)

class Topic(models.Model):
    pass
#    TOPIC_CHOICES = [
#        (0, "Opinion"),
#        (1, "Consejo"),
#        (2, "Carrera"),
#        (3, "Clasificacion"),
#    ]
#
#    topic = models.IntegerField(choices=TOPIC_CHOICES, default= 1, verbose_name="TOPIC")
#
#    def __str__(self):
#        return self.get_topic_display()


class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    contenido = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    imagen = models.ImageField(
        upload_to="post",
        default="post/sample.jpg",
    )
    autor = models.ForeignKey(
        User,
        related_name="blog_posts",
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    #topic = models.ManyToManyField(Topic, verbose_name="TOPIC")
    
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
    #topic = models.ManyToManyField(Topic, verbose_name="TOPIC")
    
    def __str__(self):
        return self.texto
