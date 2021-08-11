from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView


# def homepage(request):
#     return render(request, 'core/index.html')


class HomePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/index.html')

# class HomePage(TemplateView):
#     template_name = 'core/index.html'