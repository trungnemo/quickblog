from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models

class SignUpForm(UserCreationForm):
    email = forms.EmailField() 

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    #Later on , overwrite this function to see the dif
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        #Loop all the fields and hide all the desc on the text field
        for fieldname in ['username','email','password1','password2']:
            self.fields[fieldname].help_text = None