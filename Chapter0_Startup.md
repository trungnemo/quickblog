# Startup

- Create djangoproject: quickblog
- Create django app: blog


## Commands for startups
- Create a django project
```bash
django-admin startproject quickblog
```
-Create django app
```python
python manage.py startapp blog
```
-Then we add a blog to the INTALLED_APPS in the settings.py
```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog'
]
```
- We add templates folder into the Project folder same level as blog 
- In the templates, we add blog and partials folders
```bash
quickblog
+blog
+quockblog
+templates
--blogs
---index.html
---about.html
--partials
---base.html
---nav.html
```
- We add the template path to the TEMPLATES in the setttings.py
```python

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
- We include the blog.urls into the quickblog.urls. quickblock is the main project
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]
```
## Add Bootstraps to the template files
- We add a base.html in to the partials
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!--Page Title-->
    {% block title %}
    {% endblock %}
</head>
<body>
    <!--Page Content-->
    {% block content %}
    {% endblock %}
</body>
</html>
```
- Go to [bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
- Copy css
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
```
- Copy js
```html
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-W8fXfP3gkOKtndU4JGtKDvXbO53Wy8SZCQHczT5FMiiqmQfUpWbYdTil/SxwZgAN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.min.js" integrity="sha384-skAcpIdS7UcVUC05LJ9Dxay8AXcDYfBJqt1CJ85S/CFujBsIzCIv+l9liuYLaMQ/" crossorigin="anonymous"></script>
```
- Paste the css codes above into the head of the base.html 
- Paste the js code above into the dody of the base.html
- We will have the bootstrap base.html like this
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!--bootstrap css-->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
    <!--Page Title-->
    {% block title %}
    {% endblock %}
</head>
<body>
    <!--bootstrap js -->
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-W8fXfP3gkOKtndU4JGtKDvXbO53Wy8SZCQHczT5FMiiqmQfUpWbYdTil/SxwZgAN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.min.js" integrity="sha384-skAcpIdS7UcVUC05LJ9Dxay8AXcDYfBJqt1CJ85S/CFujBsIzCIv+l9liuYLaMQ/" crossorigin="anonymous"></script>
    <!--Page Content-->
    {% block content %}
    {% endblock %}
</body>
</html>
```
## Index and About pages
- We add the index.html and about.html into the templates\blog\
- notes: {% extends 'partials/base.html '%}
- index.html
```index.html
{% extends 'partials/base.html '%}

<!--Index Page Title-->
{% block title %}
<title>Home Page</title>
{% endblock %}

<!--Index Content -->
{% block content %}
<h1>Blog Index</h1>
{% endblock %}
```
-about.html
```html
{% extends 'partials/base.html '%}

<!--Index Page Title-->
{% block title %}
<title>About Ben Blog</title>
{% endblock %}

<!--Index Content -->
{% block content %}
<h3>About Ben Block</h3>
{% endblock %}
```
## Index and About Views in the blog\views.py
```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})

def about(request):
    return render(request, 'blog/about.html', {})
```
## Index and About path in the blog/urls.py
```python
from django.urls import path
from django.urls.resolvers import URLPattern 
from .views import index, about
urlpatterns = [
    path('', index, name = "index"),
    path('about', about, name = "about"),
]
```
- Now we run the web for testing
```bash
python manage.py runserver
```

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
## License
[KenBroTech Videos](https://www.youtube.com/playlist?list=PLInvlTu9nmo9Saxdd70M4f0m5jcPrWXd7)
