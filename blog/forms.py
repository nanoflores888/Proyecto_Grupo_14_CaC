from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):
            
        class Meta:
            model = Post
            exclude = ("status", "created_on", "updated_on", "topic")

            widgets = {
                "titulo": forms.TextInput(attrs={"class": "form-control"}),
                "slug": forms.TextInput(attrs={"class": "form-control"}),
                "contenido": forms.Textarea(attrs={"class": "form-control content"}),
                "imagen": forms.FileInput(attrs={"class": "form-control"}),
                "autor": forms.HiddenInput(),
            }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            "post",
            "autor",
            "texto",
        )

        widgets = {
            "post": forms.HiddenInput(),
            "autor": forms.HiddenInput(),
            "texto": forms.Textarea(attrs={"class": "form-control content"}),
        }
