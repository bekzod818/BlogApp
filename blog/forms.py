from django.forms import ModelForm, TextInput, Textarea, FileInput, Select
from .models import Post, Comment



class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'photo', 'body', 'publish', 'status']
        widgets = {
            'photo': FileInput(attrs={
                'class': 'form-control'
            }),   
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
    
        widgets = {
                'body': Textarea(attrs={
                    "rows": 3,
                    "class": "form-control",
                    "placeholder": "Write your comment ...",
                })
            }