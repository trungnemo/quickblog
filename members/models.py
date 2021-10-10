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
