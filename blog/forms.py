from django import forms

from .models import Comment, Post


<<<<<<< HEAD
class PostForm(forms.ModelForm):        
        class Meta:
            model = Post
            exclude = ("status", "created_on", "updated_on", "topic")
=======
class PostForm(forms.ModelForm):
     topic = forms.ModelChoiceField(queryset= Topic.objects.all(),  # Verifica que el queryset sea iterable
                                    widget=forms.Select(attrs={"class": "form-control"}))
     
     class Meta:
        model = Post
        exclude = ("status", "created_on", "updated_on")
>>>>>>> 4ea3cbccfd2da0339a57df5cdcfcff6f63a48791

        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "contenido": forms.Textarea(attrs={"class": "form-control content"}),
            "imagen": forms.FileInput(attrs={"class": "form-control"}),
            #"autor": forms.HiddenInput(),
            }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            "post",
            "autor",
            "texto",
<<<<<<< HEAD
=======
            "topic",
>>>>>>> 4ea3cbccfd2da0339a57df5cdcfcff6f63a48791
        )

        widgets = {
            "post": forms.HiddenInput(),
            "autor": forms.HiddenInput(),
            "texto": forms.Textarea(attrs={"class": "form-control content"}),
<<<<<<< HEAD
=======
            "topic" : forms.Select(attrs={"class": "form-control"}),
>>>>>>> 4ea3cbccfd2da0339a57df5cdcfcff6f63a48791
        }
