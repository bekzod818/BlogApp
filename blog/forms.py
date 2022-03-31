from django.forms import ModelForm, TextInput, Textarea, FileInput, Select
from .models import Post


class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'photo': FileInput(attrs={
                'class': 'form-control'
            }),   
        }