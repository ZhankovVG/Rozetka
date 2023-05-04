from django.shortcuts import render
from .models import *
from django.views.generic import ListView


class  ElectronicsDeviceViews(ListView):
    model = ElectronicsDevice
    queryset = ElectronicsDevice.objects.filter(draft=False)