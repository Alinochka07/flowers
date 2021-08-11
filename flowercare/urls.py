from django.urls import path
from .views import flower_care


urlpatterns = [
    path('', flower_care, name='flower-care'),
]