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