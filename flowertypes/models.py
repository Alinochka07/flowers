from django.db import models
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone



class RosesBouquets(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='roses', null=True, blank=True)
    image2 = models.ImageField(upload_to='roses', null=True, blank=True)
    sale = models.IntegerField('Discount percentage', null=True, blank=True, default=0)
    

    def get_sale(self):
        price = int(self.price * (100 - self.sale) / 100)
        return price

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Букет из роз"
        verbose_name_plural = "Букеты из роз"
        ordering = ['name']

# class Product(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     category = models.ForeignKey(RosesBouquets, on_delete=models.CASCADE)



class SeasonFlowers(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='seasonal', null=True, blank=True)
    sale = models.IntegerField('Discount percentage', null=True, blank=True, default=0)

    def get_sale(self):
        price = int(self.price * (100 - self.sale) / 100)
        return price

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сезонный букет"
        verbose_name_plural = "Сезонные букеты"
        ordering = ['name']


class AssortedFlowers(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='assorted', null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    sale = models.IntegerField('Discount percentage', null=True, blank=True, default=0)

    def get_sale(self):
        price = int(self.price * (100 - self.sale) / 100)
        return price

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ассорти букет"
        verbose_name_plural = "Ассорти букеты"
        ordering = ['name']





#     title = models.CharField(max_length=150)
#     date = models.DateTimeField()
#     author = models.ForeignKey(setting.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)


# class Comment(models.Model):
#     review = models.ForeignKey('review.Review', on_delete=models.CASCADE, related_name='comments', null=True)
#     author = models.ForeignKey(setting.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
#     text = models.TextField(max_length=300)
#     created_date = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.text









