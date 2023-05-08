from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


class CategoryMix:
    # Category output
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] = Category.objects.all()
        return context


class HouseholdAppliancesView(CategoryMix, ListView):
    # Output of all products
    model = WashingMachine
    queryset = WashingMachine.objects.filter(draft=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['washingMachine_list'] = WashingMachine.objects.filter(
            draft=False)
        return context


# class ElectronicsDeviceViews(CategoryMix, ListView):
#     model = ElectronicsDevice
#     queryset = ElectronicsDevice.objects.filter(draft=False, by_action=False)
