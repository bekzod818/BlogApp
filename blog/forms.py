from attr import attrs
from django import forms
from django.forms import ModelForm, TextInput, Textarea, FileInput, Select
from .models import Post, Comment
from captcha.fields import CaptchaField



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


class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50)
    email = forms.EmailField(label="Email")
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()