# Blog CRUD (Create, Read, Update, Delete)
- 
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
from django.db.models.base import Model

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class   Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titlle + ", " + self.author.username
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



## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
## License
[KenBroTech Videos](https://www.youtube.com/playlist?list=PLInvlTu9nmo9Saxdd70M4f0m5jcPrWXd7)
