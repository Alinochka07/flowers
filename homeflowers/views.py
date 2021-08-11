from django.shortcuts import render
from .models import HomeFlowers



def home_flowers(request):
    h_flowers_objects = HomeFlowers.objects.all()
    return render(request, 'homeflowers.html',
    {'homeflowers': h_flowers_objects})
