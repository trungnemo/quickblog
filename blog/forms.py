from django import forms
from .models import Post 

#To input post
class PostForm(forms.ModelForm):
    #Set the number of rows for the content inputs in the form
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        model = Post
        fields = ('title','content')