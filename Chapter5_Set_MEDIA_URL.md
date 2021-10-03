# Set the parameter  MEDIA_URL, MEDIA_ROOT
- When a user upload images to a folder, we need to seet the media STATIC file so Web app can file the url to display the images
- Uploading here is for example we declare the models.ImageField(upload_to='profile')
- We go to [django online doc](https://docs.djangoproject.com/en/3.2/howto/static-files/), and follow the guides

## Edit the DjangoProject urls.py
- We go to the Djngo Online Doc, and copy the codes
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
- We go to the DjangoProject folder (BenLogger) and edit the urls.py
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('members.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


```
## Edit the DjangoProject settings.py by adding codes
```python
#....
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

STATIC_ROOT = BASE_DIR / 'asset'

```
## Test the settings
- At the Command, run to check the settings
```bash
python manage.py collectstatic
```
- Run the Web and go django to upload images for a model with image field
- THen view it

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)
## License
[KenBroTech Videos](https://www.youtube.com/playlist?list=PLInvlTu9nmo9Saxdd70M4f0m5jcPrWXd7)
