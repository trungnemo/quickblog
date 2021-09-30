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
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def sign_up(request):
    return render(request, 'memebrs/sign_up.html', {})

```
- We create a new folder named members in the templates folder
- We add a sign_up.html
```html
    {% extends 'partials/base.html '%}
    {% load crispy_forms_tags %}
    <!--Index Page Title-->
    {% block title %}
    <title>Sign up </title>
    {% endblock %}

    {% block content %}
    <h3>New User Registration Form</h3>
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
    path('sign_up', sign_up, name = 'member-sign-up' ),
] 
```
- We add the members.urls.py into the django project (BenLoggers) urls.py
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('members', include('members.urls'))
```



## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
## License
[KenBroTech Videos](https://www.youtube.com/playlist?list=PLInvlTu9nmo9Saxdd70M4f0m5jcPrWXd7)
