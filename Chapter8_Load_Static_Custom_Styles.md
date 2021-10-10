# {% load static %} to apply custom styles for base.html

## Set the PATH for all static files
- Create a new static dir into the root same level as django project, here we have the project folder trees
```bash
BenLoggers
+ assets
+ blog
+ media
+ members
+ benloggers[django project folder]
+ static
+ templates
- db.sqlite3
- manage.py
- requirements.txt
```

- Add the STATICFILES_DIRS into the django project settings.py
```python

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
```

## Add style.css for the base.html
- download the [backgroud.jpg](https://github.com/trungnemo/quickblog/blob/master/media/background.jpg)  and add it to the media folder
- add style.css into the static dir
```css
.cover{
    background: url('/media/background.jpg');
    background-position: center;
    background-size: cover;
    height: 100vh;
}
```
- load static for the base.html
```html
<!--add this at the top of the page-->
{% load static %}

<!--Add this in the <head> </head> of the base.html
<!--apply custom styles in style.css for the base.html -->
<link rel="stylesheet" href="/static/style.css">

```
- We add div with class = "cover" for the login and signup
```html
    <!--Add this div with class cover for the background images with the !important -> the important will overwrite the bootstrap class-->
    <div class="cover">
        <div class="container">
         ...
        </div> 
    </div>
```
- login.html
```html
    {% extends 'partials/base.html '%}
    {% load crispy_forms_tags %}
    <!--Index Page Title-->
    {% block title %}
    <title>Benloggers Login</title>
    {% endblock %}

    {% block content %}
    <!--Add this div with class cover for the backgroud images with the !important -> the important will overwrite the bootstrap class-->
    <div class="cover">
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
                                <div class="d-grid gap-2">
                                    <button class="btn btn-primary" type="submit">Login</button>
                                </div>
                            </form>
                            <hr/>
                            <div class="text-center my-3">
                                <a href="">Forget Password</a>
                            </div>
                            <hr/>
                            <div class="text-center my-3">
                                <a href="{% url 'member-sign-up'%}" class="btn btn-success">Create an account</a>
                            </div>
                        
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {% endblock %}
```

 

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
## License
[KenBroTech Videos](https://www.youtube.com/playlist?list=PLInvlTu9nmo9Saxdd70M4f0m5jcPrWXd7)
