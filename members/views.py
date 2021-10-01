from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
# Create your views here.

def sign_up(request):
    
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form  = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        #form = UserCreationForm()
        form = SignUpForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'members/sign_up.html', context)

