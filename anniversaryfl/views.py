from django.shortcuts import render
from .models import AnniversaryFlowers



def anniversary(request):
    a_flowers_objects = AnniversaryFlowers.objects.all()
    return render(request, 'anniversary.html', 
    {'anniversaryfl': a_flowers_objects})

