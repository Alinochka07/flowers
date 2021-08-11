from django.shortcuts import render
from .models import FlowersBouquets



def flowers(request):
    flowers_objects = FlowersBouquets.objects.all()
    return render(request, 'flowers.html',
    {'flowertypes': flowers_objects})