from django.urls import path
from django.conf.urls import url
from .views import *



urlpatterns = [
    path('rosesbouquets/', roses_bouquets, name='roses-bouquets'),
    path('rosesbouquets/<int:id>/', rose, name='rose'),
    path('seasonal/', season_bouquets, name='season-bouquets'),
    path('seasonal/<int:id>/', season, name='season'),
    path('assorted/', assorted_bouquets, name='assorted-bouquets'),
    path('assorted/<int:id>/', assorted, name='assorted'),
]