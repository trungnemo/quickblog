from django import forms
from .models import Post 

#To input post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content')