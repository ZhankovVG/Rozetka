from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from django.db.models import Q



class CategoryMix:
    # Category output
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] = Category.objects.all()
        context['washingMachine_list'] = WashingMachine.objects.filter(
            draft=False)
        context['search_query'] = self.request.GET.get('q')
        return context


class HouseholdAppliancesView(CategoryMix, ListView):
    # Output of all products
    model = WashingMachine
    queryset = WashingMachine.objects.filter(draft=False)


class SearchViews(CategoryMix, ListView):
    template_name = 'main/washingMachine_list.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        query = self.request.GET.get('q')
    
        # electro_qs = ElectronicsDevice.objects.filter(Q(name__icontains=query) | Q(code__icontains=query))
        hfridge_qs = Hfridge.objects.filter(Q(name__icontains=query) | Q(name__icontains=query))
        # washing_qs = WashingMachine.objects.filter(Q(name__icontains=query) | Q(code__icontains=query))

        qs = hfridge_qs.union(hfridge_qs)

        return qs 