from django.urls import path
from .views import anniversary


urlpatterns = [
    path('', anniversary, name='anniversary-flowers'),
]