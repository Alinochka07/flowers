from django.urls import path
from .views import *



urlpatterns = [
    path('rosesbouquets/', roses_bouquets, name='roses-bouquets'),
    path('<int:id>/', rose, name='rose'),
    path('otherbouquets/', other_bouquets, name='other-bouquets'),
    path('<int:id>/', other, name='other'),
    path('seasonal/', season_bouquets, name='season-bouquets'),
    path('<int:id>/', season, name='season'),
]