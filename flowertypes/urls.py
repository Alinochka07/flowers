from django.urls import path
from .views import *



urlpatterns = [
    # path('', flowers, name='flower-types'),
    path('rosesbouquets/', roses_bouquets, name='roses-bouquets'),
    path('<int:id>/', rose, name='rose'),
    path('otherbouquets/', other_bouquets, name='other-bouquets'),
    path('<int:id>/', other_flowers, name='other-flowers'),
]