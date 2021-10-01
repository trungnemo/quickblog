from django.urls import path
from django.urls  import path
from .views import sign_up

urlpatterns = [
    path('sign_up/', sign_up, name = 'member-sign-up' ),
] 