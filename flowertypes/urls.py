from django.urls import path
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from flowertypes.models import *
from . import views
from .views import *


# app_name = ['roses-bouquets', 'rose', 'season-bouquets', 'season', 'assorted-bouquets', 'assorted']
urlpatterns = [
    # url(r'^$', ListView.as_view(
    #     queryset = RosesBouquets.objects.all(),
    #     template_name = "flowertypes/flowers.html"
    # )),
    path('rosesbouquets/', roses_bouquets, name='roses-bouquets'),
    path('rosesbouquets/<int:id>/', rose, name='rose'),
    path('seasonal/', season_bouquets, name='season-bouquets'),
    path('seasonal/<int:id>/', season, name='season'),
    path('assorted/', assorted_bouquets, name='assorted-bouquets'),
    path('assorted/<int:id>/', assorted, name='assorted'),
]