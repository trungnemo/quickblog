# Member User Sign Up
We create a new django app named members, this app will
- let users to register member accounts
- login and log out

## Create django app : members
- Execute the command
```bash
python manage.py createapp members
```
- Add the new app to the django project settings.py
```python

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'members.apps.MembersConfig',
    'crispy_forms'
]

```
## Register User/ Create a new member
- We start at the members/views.py
```python
from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def sign_up(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'members/sign_up.html', context)

```
- We create a new folder named members in the templates folder
- We add a sign_up.html
```html
    {% extends 'partials/base.html '%}
    {% load crispy_forms_tags %}
    <!--Index Page Title-->
    {% block title %}
    <title>Member sign up </title>
    {% endblock %}

    {% block content %}
    <div class="container">
        <div class="row mt-5 pt-3">
            <div class="col-md-5 offset-md-6">
                <div class="card my-3 shadow">
                    <div class="card-body">
                        <h4>Benloggers Member Signup</h4>
                        <hr/>
                        <form method = "POST" >
                            {% csrf_token %}
                            {{ form|crispy }}
                            <br/> 
                            <input type="submit" class="btn btn-primary btn-block" value="Sign up">    
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {% endblock %}
```
- We add a new file urls.py into the members folder app
```bash
-BenLoggers
--members
---urls.py
```
```python
from django.urls import path
from django.urls  import path
from .views import sign_up

urlpatterns = [
    path('sign_up/', sign_up, name = 'member-sign-up' ),
] 
```
- We INCLUDE the urls.py of members app into the django project (BenLoggers) urls.py
```python
from django.urls import path
from django.urls.resolvers import URLPattern 
from .views import index, about
urlpatterns = [
    path('', index, name = "index"),
    path('about', about, name = "about"),
]
```
- Now we can run the server and try to register a user test
```bash
python managre.py runserver
```

## Improve the signup with our customized SignupForm 
- We add a new file forms.py into the members
- We add a class SignUpForm 
```python
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
```
- We use this form by adding to the members.views.py
```python
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
```
- Now run the Web server to test the improvement
```bash
python manage.py runserver
```
## Disable Password strength verification
- Disable by add this config value into the django project settings.py
```python
AUTH_PASSWORD_VALIDATORS = []
```

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
## License
[KenBroTech Videos](https://www.youtube.com/playlist?list=PLInvlTu9nmo9Saxdd70M4f0m5jcPrWXd7)
