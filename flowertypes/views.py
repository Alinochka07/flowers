from django.shortcuts import render, HttpResponse
from .models import *



def flowers(request):
    flowers_objects = FlowersBouquets.objects.all()
    return render(request, 'flowers.html',
    {'flowertypes': flowers_objects})


def roses_bouquets(request):
    roses_bouquets_objects = RosesBouquets.objects.all()
    return render(request, 'roses.html',
    {'flowertypes': roses_bouquets_objects})

def roses(request, id):
    try:
        roses_object = RosesBouquets.objects.get(id=id)
        return render(request, 'roses/roses.html', {
            'roses_object': roses_object
        })
    except RosesBouquets.DoesNotExist as e:
        return HttpResponse(f'Товар не существует: {e}', status=404)

