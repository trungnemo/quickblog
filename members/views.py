from django.contrib.auth import forms
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.

def sign_up(request):
    
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form  = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member-login') #redirect('index')
    else:
        #form = UserCreationForm()
        form = SignUpForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'members/sign_up.html', context)


def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST or None, instance = request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance = request.user.profile) 

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('member-profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'members/profile.html', context)