from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
    path('', flowers, name='flower-types'),
    path('', roses_bouquets, name='roses-bouquets'),
]