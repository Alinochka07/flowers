from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView




class HomePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/index.html')

