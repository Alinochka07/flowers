from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from .models import *



class FlowersBouquets(models.Model):
    # user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    # description = models.TextField(null=True, blank=True)
    # price = models.IntegerField(null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # views_count = models.IntegerField(default=0)
    # image = models.ImageField(upload_to='flowertypes', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цветы и букеты"
        verbose_name_plural = 'Цветы и букеты'
        ordering = ['name']


class RosesBouquets(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='roses', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Букеты из роз"
        verbose_name_plural = "Букеты из роз"
        ordering = ['name']
        # fields = ['name', 'description', 'price', 'image']

