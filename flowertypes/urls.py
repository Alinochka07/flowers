from django.urls import path
from .views import flowers


urlpatterns = [
    path('', flowers, name='flower-types'),
]