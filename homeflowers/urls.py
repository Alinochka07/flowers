from django.urls import path
from .views import home_flowers


urlpatterns = [
    path('', home_flowers, name='home-flowers'),
]