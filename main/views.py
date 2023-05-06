from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView



class ElectronicsDeviceViews(ListView):
    model = ElectronicsDevice
    queryset = ElectronicsDevice.objects.filter(draft=False, by_action=False)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] = Category.objects.all()
        return context

class CategoryViews(DetailView):

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] = Category.objects.all()
        return context
