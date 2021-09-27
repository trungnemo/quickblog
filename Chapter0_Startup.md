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
- We add a templates folder to a blog folder/app
- We add a base.html in to the templates
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
    {% block title %}
    {% endblock %}
</body>
</html>
```
- We add a urls.py into the blog folder
```python
#THe list of path for the views in the blog
from django.urls import path
from django.urls.resolvers import URLPattern 

urlpatterns = [
    
]
```
- We include the blog.urls into the quickblog.urls. quickblock is the main project
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog/urls'))
]
```

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
## License
[KenBroTech Videos](https://www.youtube.com/playlist?list=PLInvlTu9nmo9Saxdd70M4f0m5jcPrWXd7)
