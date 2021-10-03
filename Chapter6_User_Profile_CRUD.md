# User Profile (extra user info)
## Profile model class/DB Profile model
- We create a Profile model and migrate it to the DB
- we add class Profile into the members\models.py
```python
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.files import ImageField 
from django.core.validators import FileExtensionValidator
# Create your models here.

class Profile(models.Model):
    #Relation ship with django.auth User: one user has one profile (extra info)
    user = models.OneToOneField(User, on_delete=models.Case)
    #Declare to upload the profile image, with files of png, jpg
    #the upload_to where to store the file at the server side, we need to declare the STATIC
    image = models.ImageField(default = 'default.png', upload_to = 'profile', validators = [FileExtensionValidator(['png', 'jpg'])])

    def __str__(self):
        return self.user.username

```
- at the command, check if the Pillow is intalled if not then do it
```bash
pip freeze
pip intall Pillow='8.3.2'
```
- Then migrate the Profile class to the DB
```python
python manage.py makemigrations
python manage.py migrate 
```
- Register the Profile for the django dashboard admin at the members\admin.py
```python
from django.contrib import admin
from .models import Profile
# Register your models here.
admin.site.register(Profile)
```
- Download the [default.png](https://github.com/trungnemo/quickblog/blob/main/default.png)
- Add file files to the media folder 


## View for Profile page

```python
def profile(request):
    return render(request, 'members/profile.html', {})
```
## Profile html page
- We add the profile.html to the folder templates\members\
- We go to the https://getbootstrap.com/docs/5.1/components/modal/..to copy the modal (window dialog) to show up the profile edit window
```html
{% extends 'partials/base.html'%}
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
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary btn-sm">Save changes</button>
      </div>
    </div>
  </div>
</div>
{% endblock%}
```
- We add the profile path into the members\urls.py
```python
from django.urls import path
from django.urls  import path
from .views import profile, sign_up
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sign_up/', sign_up, name = 'member-sign-up' ),
    #path('login/', auth_views.LoginView.as_view(template_name ='members/login.html'), name = 'member-login' ),
    path('', auth_views.LoginView.as_view(template_name ='members/login.html'), name = 'member-login' ),
    path('profile/', profile, name = 'member-profile' ),
    path('logout/', auth_views.LogoutView.as_view(template_name ='members/logout.html'), name = 'member-logout' ),
]  

```
- Now we update the profile link on the templates\partials\navbar.html
```
 <li><a class="dropdown-item" href="{% url 'member-profile' %}">Profile</a></li>
```

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
## License
[KenBroTech Videos](https://www.youtube.com/playlist?list=PLInvlTu9nmo9Saxdd70M4f0m5jcPrWXd7)
