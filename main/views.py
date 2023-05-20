from django.shortcuts import get_object_or_404
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
    paginate_by = 5


class SearchViews(CategoryMix, ListView):
    # Search products
    def get_queryset(self):
        query = self.request.GET.get('search')
        return Product.objects.filter(
            Q(name__icontains=query) | Q(code__icontains=query)
            )
    

class DetailProductView(CategoryMix, DetailView):
    model = Product
    slug_field = 'url'


class CategoryOutputView(CategoryMix, ListView):
    model = Product
    template_name = 'main/product_list.html'
    paginate_by = 5

    def get_queryset(self):
        category = get_object_or_404(Category, url=self.kwargs['cat_slug'])
        return Product.objects.filter(category=category, draft=False)