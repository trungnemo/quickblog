# Signal when user is created then the profile is also done

- We user the django Signals
- Triger when a new member/user is registered/created then the associated profile will be created too

## signals.py
- We add a new file signals.py into the django app/folder memebrs
```python
# By TrungVan
# Date: 20211006 
# ToDo: Signal when a new user is created then create the profile

from django.contrib.auth.models import User 
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user = instance)
```
- Add codes to the members\apps.py
```python
from django.apps import AppConfig


class MembersConfig(AppConfig):
    name = 'members'

    #For the signals members.signal.create_profile
    def ready(self):
        import members.signals
```
-Edit the members.py after registration is OK, then redirect to the login page
```python
from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
# Create your views here.

def sign_up(request):
    
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form  = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member-login') #redirect('index')
    else:
        #form = UserCreationForm()
        form = SignUpForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'members/sign_up.html', context)


def profile(request):
    return render(request, 'members/profile.html', {})
```

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
## License
[KenBroTech Videos](https://www.youtube.com/playlist?list=PLInvlTu9nmo9Saxdd70M4f0m5jcPrWXd7)
