# Edit Profile - Window Popup / Modal Edit Form
- We add functionality to show up the POPUP / MODAL form to let user to edit his or her profile informations

## Start at members\forms.py
- We add UserUpdateForm and ProfileUpdateForm into the forms.py
```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import Profile

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

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'email']
    # THis __init__ will remove the desc note on the form
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        #Loop all the fields and hide all the desc on the text field
        for fieldname in ['username','email']:
            self.fields[fieldname].help_text = None
            
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['image']   
```
# Profile Update Views
- We edit the def profile(request.POST): 
```python
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
```
## Profile.html
```html
{% extends 'partials/base.html'%}
{% load crispy_forms_tags %}
<!--Page title-->
{% block title %}
<title>Profile</title>
{% endblock%}
<!--Page Content-->
{% block content %}
<div class="container">
    <!--Bootstrap style: Row in container, margin top 5, padding top 3-->
    <div class="row mt-5 pt-3">
        <!--A COLUM with 6 parts in the row, spaing from the right and left is 3 parts -->
        <div class="col-md-6 offset-md-3">
            <dif class="card my-3 shadow">
                <div class="card-body">
                    <!--Each Row contains 12 col-->
                     <div class="row"> 
                        <span class="h4">Profile Page</span>
                        <!-- Button trigger modal -->
                        <span>
                            <button type="button" class="btn btn-info btn-sm float-right " data-bs-toggle="modal" data-bs-target="#modalEditProfile">
                                Edit Profile
                            </button>
                        </span>  
                        <hr/>
                        <!--This takes 4 cols in the 6 cell COL above (col-md-6)-->
                        <div class="col-md-4">
                            {% if user.profile.image %}
                                <img 
                                    src="{{ user.profile.image.url }}" 
                                    alt="Profile Img"
                                    width="100px" 
                                    height="100px"
                                    >
                            {% else %}
                                <img
                                    src="https://i.pravatar.cc/50" 
                                    width="100px" 
                                    height="100px"            
                                    class="rounded-circle"
                                    />
                            {% endif %}
                        </div>   
                        <div class="col-md-8">
                            <h4>Name: {{ user.username }}</h4>
                            <h4>Email: {{ user.email  }}</h4>
                        </div>
                     </div>   
                </div>
            </dif>
        </div>
    </div>
</div>

<!--Modal to show up the edit profile window-->


<!-- Modal -->
<div class="modal fade" id="modalEditProfile" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Edit Profile</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div class="row">
          <div class="col-md-4">
             {% if user.profile.image %}
                  <img 
                    src="{{ user.profile.image.url }}" 
                    alt="Profile Img"
                    width="100px" 
                    height="100px"
                    >
              {% else %}
                  <img
                    src="https://i.pravatar.cc/50" 
                    width="100px" 
                    height="100px"            
                    class="rounded-circle"
                  />
            {% endif %}
          </div>
          <div class="col-md-8">
            <form method="POST" enctype="multipart/form-data" >
              {% csrf_token %} 
              {{ u_form|crispy }}
              {{ p_form|crispy }}
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Close</button>
                <button type="submit" class="btn btn-primary btn-sm">Update</button>
              </div>
            </form>
          </div>
        </div>
      </div>
     
    </div>
  </div>
</div>
<!--end of Edit Profile Modal-->

{% endblock%}
```

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
## License
[KenBroTech Videos](https://www.youtube.com/playlist?list=PLInvlTu9nmo9Saxdd70M4f0m5jcPrWXd7)
