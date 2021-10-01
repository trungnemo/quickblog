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



## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
## License
[KenBroTech Videos](https://www.youtube.com/playlist?list=PLInvlTu9nmo9Saxdd70M4f0m5jcPrWXd7)
