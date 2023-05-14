from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from django.db.models import Q



class CategoryMix:
    # Category output
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] = Category.objects.all()
        context['washingMachine_list'] = self.get_queryset()
        return context


class HouseholdAppliancesView(CategoryMix, ListView):
    # Output of all products
    model = WashingMachine
    queryset = WashingMachine.objects.filter(draft=False)


class SearchViews(CategoryMix, ListView):
    # Search products
    def get_queryset(self):
        return WashingMachine.objects.filter(name__icontains=self.request.GET.get('search'))