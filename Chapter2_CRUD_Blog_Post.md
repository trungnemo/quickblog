# Blog CRUD (Create, Read, Update, Delete)
We add functionalities to
- List (Read) all posts
- Create (Add) a new post, Update a post , Delete a Post
## Blog model
- Create a class Blog in the models.py, to hold the blog post information
- The Model model has a relationship with the registered users/members, cause only members can upload a new post, so he/she becomes an authors of a post
- The relation ships is: One Author can have many posts
- First we migrate the default django user authentication and create a admin user
```bash
python manage.py migrate
python manage.py createsuperuser
(user name is : admin, password is ben123)
```
- Then we create a class Blog in the blog\models.py
```python
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class   Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        #Order the list of Post.objects.all() or filter() by date by DESC
        ordering = ('-date_created', ) #if no , at the end it  will be errornous

    def __str__(self):
        return self.title + ", " + self.author.username
```
- We register the Post model tobe managed the django dashboard admin
- We do it in the blog\admin.py
```python
from django.contrib import admin
from .models import Post
# Register your models here
#admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created']
    list_filter = ['title']

admin.site.register(Post, PostAdmin)
```
- Now we migrate the Post class into the DB
```bash
python manage.py makemigrations
python manage.py migrate
```
- We run the web server and goto http://127.0.0.1:8000/admin
- We add some posts
```bash
python manage.py runserver
```
## List blog posts (Read) on the index.html
- We edit the index in the blog\views.py
```python
# Create your views here.
def index(request):
    #Use the django ORM framework to get the data 
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts':posts})
```
- We edit ./templates/blog/index.html
- We add the {% for p in posts %} at <div class = "col-md-8">
```html
{% extends 'partials/base.html '%}

<!--Index Page Title-->
{% block title %}
<title>Home Page</title>
{% endblock %}

<!--Index Content -->
{% block content %}
<div class="container">
        <H3 class="text-center" >BenBlog</H3>
        <!--The row contains 12 cols of bootstrap-->
        <div class="row mt-2 pt-5">
            <!--The Left Pain: for the Menu: it takes 4 columns-->
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body shadow">
                        <h3>Add a Post Form here</h3>
                    </div>
                </div>
            </div>
            <!--The Right Pain: for Post Index: it takes 8 columns-->
            <div class="col-md-8">
                <!--We use the card for each post-->
                <div class="card">
                    <div class="card-body">
                        {% for p in posts %}
                        <!--A Post 1 -->
                        <div class="row">
                            <div class="col-md-4">
                                <img src="" alt="Post Image">
                            </div>
                            <div class="col-md-8">
                                <!--post 1-->
                               <div class="card shadow my-2">
                                    <small>{{ p.date_created }}</small>
                                    <hr/>
                                    <a class="h3" href="">{{ p.title }}</a>
                                    <p class="text-justify p-3">
                                        {{ p.content|safe }}
                                    </p>
                               </div>
                              
                            </div>
                        </div>
                        {% endfor %}
                    </div>
                </div>
            </div>
        </div>
    </div>
{% endblock %}
```
## Create A Post
- We add a new file forms.py into the blog folder
- We add a class PostForm 
```python
from django import forms
from .models import Post 

#To input post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content')
```
- We add a PostForm to the index view for creating a Post
```python
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.

# def index(request):
#     #Use the django ORM framework to get the data 
#     posts = Post.objects.all()
#     return render(request, 'blog/index.html', {'posts':posts})


def index(request):
    #Use the django ORM framework to get the data 
    posts = Post.objects.all()
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            #Get the instance form the save but not commit the data to the DB, in mem
            instance = form.save(commit=False)
            #Set the author for the created post form
            instance.author = request.user
            #Save to the DB with the author is the logon user
            instance.save()
            #after save OK, redirect the page to the index page, the names are defined in the urls.py
            return redirect('index')
    else:
        form = PostForm()

    context = {
        'posts':posts,
        'form': form
    }
    return render(request, 'blog/index.html', context)
```
- We add a form to the templates/blog/index.html
```html
{% extends 'partials/base.html '%}

<!--Index Page Title-->
{% block title %}
<title>Home Page</title>
{% endblock %}

<!--Index Content -->
{% block content %}
<div class="container">
        <!--The row contains 12 cols of bootstrap-->
        <div class="row pt-5">
            <!--The Left Pain: for the Menu: it takes 4 columns-->
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body shadow">
                        <form action="POST">
                            {{ form }}
                            <br/>
                            <input type="submit" class="btn btn-primary" value="Post">
                        </form>
                    </div>
                </div>
            </div>
            <!--The Right Pain: for Post Index: it takes 8 columns-->
            <div class="col-md-8">
                <!--We use the card for each post-->
                <div class="card">
                    <div class="card-body">
                        {% for p in posts %}
                        <!--A Post 1 -->
                        <div class="row">
                            <div class="col-md-4">
                                <img src="" alt="Post Image">
                            </div>
                            <div class="col-md-8">
                                <!--post 1-->
                               <div class="card shadow my-2">
                                    <small>{{ p.date_created }}</small>
                                    <hr/>
                                    <a class="h3" href="">{{ p.title }}</a>
                                    <p class="text-justify p-3">
                                        {{ p.content|safe }}
                                    </p>
                               </div>
                              
                            </div>
                        </div>
                        {% endfor %}
                    </div>
                </div>
            </div>
        </div>
    </div>
{% endblock %}
```
## Improve the Input form with crispy package
- We install the crispy to improve the input form

```bash
#Check if the packages installed already
pip show django-crispy-forms
#If not installed yet, then
pip install django-crispy-forms
#Update the requirements.txt of the project
pip freeze > requirements.txt
```
- We go to the [online crispy guides](https://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs) to
-   Add the crispy_forms to the INSTALLED_APPS in the settings.py of the project BenLoggers
-   Add crispy template to use
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
    'crispy_forms'
]


#cripspy template
CRISPY_TEMPLATE_PACK = 'bootstrap4'
```
- Add to our page: index.html
```html
{% extends 'partials/base.html '%}
{% load crispy_forms_tags %}
<!--Index Page Title-->
{% block title %}
<title>Home Page</title>
{% endblock %}


<!--Index Content -->
{% block content %}
<div class="container">
        <!--The row contains 12 cols of bootstrap-->
        <div class="row pt-5">
            <!--The Left Pain: for the Menu: it takes 4 columns-->
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body shadow">
                        <form action="POST">
                            {% csrf_token %}
                            {{ form|crispy }}
                            <br/>
                            <input class="btn btn-primary btn-block" type="submit"  value="Post">
                        </form>
                    </div>
                </div>
            </div>
            <!--The Right Pain: for Post Index: it takes 8 columns-->
            <div class="col-md-8">
                <!--We use the card for each post-->
                <div class="card">
                    <div class="card-body">
                        {% for p in posts %}
                        <!--A Post 1 -->
                        <div class="row">
                            <div class="col-md-4">
                                <img src="" alt="Post Image">
                            </div>
                            <div class="col-md-8">
                                <!--post 1-->
                               <div class="card shadow my-2">
                                    <small>{{ p.date_created }}</small>
                                    <hr/>
                                    <a class="h3" href="">{{ p.title }}</a>
                                    <p class="text-justify p-3">
                                        {{ p.content|safe }}
                                    </p>
                               </div>
                              
                            </div>
                        </div>
                        {% endfor %}
                    </div>
                </div>
            </div>
        </div>
    </div>
{% endblock %}

```
- If you want to set the number of rows for the content text box, we can edit the PostForm in blog\forms.oy like this
```python
from django import forms
from .models import Post 

#To input post
class PostForm(forms.ModelForm):
    #Set the number of rows for the content inputs in the form
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        model = Post
        fields = ('title','content')
```


## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
## License
[KenBroTech Videos](https://www.youtube.com/playlist?list=PLInvlTu9nmo9Saxdd70M4f0m5jcPrWXd7)
