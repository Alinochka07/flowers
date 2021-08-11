from django.shortcuts import render
from .models import FlowerCare 




def flower_care(request):
    c_flower_objects = FlowerCare.objects.all()
    return render(request, 'flowercare.html',
    {'flowercare': c_flower_objects})
