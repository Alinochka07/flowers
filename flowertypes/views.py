from django.shortcuts import render, HttpResponse
from .models import *



# def flowers(request):
#     flowers_objects = RosesBouquets.objects.all()
#     return render(request, 'flowertypes/.html')
#     # {'flowertypes': flowers_objects})


def roses_bouquets(request):
    roses_bouquets_object = RosesBouquets.objects.all()
    return render(request, 'roses.html',
    {'flowertypes': roses_bouquets_object})

def roses(request, id):
    try:
        roses_object = RosesBouquets.objects.get(id=id)
        return render(request, 'roses.html', {
            'roses_object': roses_object
        })
    except RosesBouquets.DoesNotExist as e:
        return HttpResponse(f'Товар не существует: {e}', status=404)

def other_bouquets(request):
    #  other_bouquets_objects = OtherBouquets.objects.all()
     return render(request, 'otherflowers.html')
    #  {'flowertypes': other_bouquets_objects})


def other_flowers(request):
    try:
        others_object = OtherBouquets.objects.get(id=id)
        return render(request, 'otherflowers.html', {
            'others_object': others_object
        })
    except OtherBouquets.DoesNotExist as e:
        return HttpResponse(f'Товар не существует: {e}', status=404)


def otherflowers(request, id):
    try:
        otherflowers_object = OtherBouquets.objects.get(id=id)
        return render(request, 'otherflowers.html', {
            'otherflowers_object': otherflowers_object
        })
    except OtherBouquets.DoesNotExist as e:
        return HttpResponse(f'Товар не существует: {e}', status=404)