from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from django.db.models import Q



class CategoryMix:
    # Category output
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] = Category.objects.all()
        return context


class WashingMachineView(CategoryMix, ListView):
    # Output WashingMachine
    model = Product
    queryset = Product.objects.filter(draft=False)


class SearchViews(CategoryMix, ListView):
    # Search products
    def get_queryset(self):
        query = self.request.GET.get('search')
        return Product.objects.filter(
            Q(name__icontains=query) | Q(code__icontains=query)
            )