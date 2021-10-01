# Login and Logout

This part will guide you to develop the functions for registered user tp
- login
- logout
## Login
- We inherit the views from the django.contrib.auth , so upto now we do not need to write a view for login
- We will add the LoginView of django.contrib.auth to the members\urls.py
```python
from django.urls import path
from django.urls  import path
from .views import sign_up
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sign_up/', sign_up, name = 'member-sign-up' ),
    path('login/', auth_views.LogoutView.as_view(template_name ='members/login.html'), name = 'member-login' ),
] 
```
- We create a new file named login.html in the folder templates\members\
- The codes will copy all form sign_up.html and make some small changes
```html
    {% extends 'partials/base.html '%}
    {% load crispy_forms_tags %}
    <!--Index Page Title-->
    {% block title %}
    <title>Benloggers Login</title>
    {% endblock %}

    {% block content %}
    <div class="container">
        <div class="row mt-5 pt-3">
            <div class="col-md-5 offset-md-6">
                <div class="card my-3 shadow">
                    <div class="card-body">
                        <h4>Login to Benloggers</h4>
                        <hr/>
                        <form method = "POST" >
                            {% csrf_token %}
                            {{ form|crispy }}
                            <br/>
                            <input type="submit" class="btn btn-primary btn-block" value="Login">    
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {% endblock %}
```
- We add LOGIN_REDIRECT_URL = 'index' to the settings.py of the project. So after the login, the app will redirect you to this page
```python
# Get the 'index' name at blog.urls.py -> path('', index, name = "index")
LOGIN_REDIRECT_URL = 'index'
```
## Logout
- Add the django.contrib.auth.views to the url
```python
from django.urls import path
from django.urls  import path
from .views import sign_up
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sign_up/', sign_up, name = 'member-sign-up' ),
    path('login/', auth_views.LoginView.as_view(template_name ='members/login.html'), name = 'member-login' ),
    #New path for logout
    path('logout/', auth_views.LogoutView.as_view(template_name ='members/logout.html'), name = 'member-logout' ),
]  
```
- We create a new logout.html in the the templates\members\
```html
    {% extends 'partials/base.html '%}
    {% load crispy_forms_tags %}
    <!--Index Page Title-->
    {% block title %}
    <title>Benloggers Login</title>
    {% endblock %}

    {% block content %}
    <div class="container">
        <div class="row mt-5 pt-3">
            <!--col-md-6 offset-md-6 for the center-->
            <div class="col-md-6 offset-md-3">
                <div class="card my-3 shadow">
                    <div class="card-body">
                        <h4>Logout off Benloggers</h4>
                        <hr/>
                       <div class="alert alert-info">
                           You have been logged out, See you back soon
                       </div>
                       <a href="{% url 'member-login' %}">Login</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {% endblock %}
```
## Wrapup the Signup, Login, Logout in the NavBar
```html
<nav class="navbar navbar-expand-lg navbar-primary bg-primary">
  <div class="container my-0 p-0" >
    <a class="navbar-brand text-white" href="{% url 'index' %}"> BennLoggers</a>
    <button class="navbar-toggler" type="button" 
          data-bs-toggle="collapse" 
          data-bs-target="#navbarSupportedContent" 
          aria-controls="navbarSupportedContent" 
          aria-expanded="false" 
          aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active text-white" aria-current="page" href="{% url 'index' %}">Home</a>
        </li>

      </ul>

     
       <ul class="navbar-nav ml-autho">
          {% if user.is_authenticated %}
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle text-white"
                href="#"
                id="navbarDropdown"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                  <img
                  src="https://i.pravatar.cc/50" 
                  width="30px" 
                  height="30px"            
                  class="rounded-circle"
                  />
            
                {{ user.username }}
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="#">Profile</a></li>
                <li><a class="dropdown-item" href="#">Setting</a></li>
                <li><hr class="dropdown-divider" /></li>
                <li>
                  <a class="dropdown-item" href="{% url 'member-logout' %}">Logout</a>
                </li>
              </ul>
            </li>
          {% else %} 
            <li class="nav-item">
              <a class="nav-link text-white" href="{% url 'member-sign-up' %}">Sign up</a>
            </li>
            <li class="nav-item">
              <a class="nav-link text-white" href="{% url 'member-login' %}">Login</a>
            </li>
          {% endif %}
        </ul>      
      
      
    </div>

     
  </div>
</nav>
```
- Voila, run it
```bash
python manage.py runserver
```

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
## License
[KenBroTech Videos](https://www.youtube.com/playlist?list=PLInvlTu9nmo9Saxdd70M4f0m5jcPrWXd7)
