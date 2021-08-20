from django.shortcuts import render, HttpResponse
from .models import RosesBouquets, SeasonFlowers


# Roses category


def roses_bouquets(request):
    roses_bouquets_object = RosesBouquets.objects.all()
    return render(request, 'flowers.html',
    {'rosesbouquets': roses_bouquets_object})

def rose(request, id):
    try:
        roses_object = RosesBouquets.objects.get(id=id)
        return render(request, 'roses.html', {
            'roses_object': roses_object
        })
    except RosesBouquets.DoesNotExist as e:
        return HttpResponse(f'Товар не существует: {e}', status=404)



# Other flowers category

def other_bouquets(request):
    other_bouquets_object = OtherFlowers.objects.all()
    return render(request, 'flowers2.html',
    {'otherbouquets': other_bouquets_object})



def other(request, id):
    try:
        other_object = OtherFlowers.objects.get(id=id)
        return render(request, 'others.html',
        {'other_object': other_object})

    except OtherFlowers.DoesNotExist as e:
        return HttpResponse(f'Товар не существует: {e}', status=404)


# Seasonal category      

def season_bouquets(request):
    season_bouquets_object = SeasonFlowers.objects.all()
    return render(request, 'flowers3.html',
    {"seasonbouquets": season_bouquets_object})

def season(request, id):
    try:
        season_object = SeasonFlowers.objects.get(id=id)
        return render(request, 'season.html',
        {'season_object': season_object})
    
    except SeasonFlowers.DoesNotExist as e:
        return HttpResponse(f'Товар не существует: {e}', status=404)
