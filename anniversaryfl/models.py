from django.db import models
from django.contrib import admin 
from django.contrib.auth.models import User



class AnniversaryFlowers(models.Model):
    # user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='anniversaryfl', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Букеты для торжеств"
        ordering = ['name']
