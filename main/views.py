from django.shortcuts import get_object_or_404, redirect, HttpResponse, render
from .models import *
from django.views.generic import ListView, DetailView, View
from django.db.models import Q
from .forms import *
from cart.forms import CartAddProductForm



class CategoryMixin:
    # Category output
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] = Category.objects.all()
        context['brand'] = BrandProduct.objects.all()
        context['star_form'] = RatingForm()
        context['cart_product_form'] = CartAddProductForm
        return context


class WashingMachineView(CategoryMixin, ListView):
    # Output WashingMachine
    model = Product
    queryset = Product.objects.filter(draft=False)
    paginate_by = 5


class SearchViews(CategoryMixin, ListView):
    # Search products
    def get_queryset(self):
        query = self.request.GET.get('search')
        return Product.objects.filter(
            Q(name__icontains=query) | Q(code__icontains=query)
        )


class DetailProductView(CategoryMixin, DetailView):
    # Full product description
    model = Product
    slug_field = 'url'


class CategoryOutputView(CategoryMixin, ListView):
    # Product listing by category
    model = Product
    template_name = 'main/product_list.html'
    paginate_by = 5

    def get_queryset(self):
        category = get_object_or_404(Category, url=self.kwargs['cat_slug'])
        return Product.objects.filter(category=category, draft=False)


class BrandOutputView(CategoryMixin, ListView):
    # Brand output
    model = Product
    template_name = 'main/product_list.html'
    paginate_by = 5

    def get_queryset(self):
        brand = get_object_or_404(BrandProduct, url=self.kwargs['brand_slug'])
        return Product.objects.filter(brand=brand)


class ReviewsView(CategoryMixin, View):
    # Adding a comment
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())


class AddStarsRating(View):
    # Adding a rating
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                product_id=int(request.POST.get("product")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class PersonalCabinetView(View):
    # User profile
    def get(self, request):
        user = request.user
        profile, created = UserProfile.objects.get_or_create(user=user)
        form = UserProfileForm(instance=profile)
        context = {'form': form}
        return render(request, 'main/profile.html', context)

    def post(self, request):
        user = request.user
        profile, created = UserProfile.objects.get_or_create(user=user)
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        context = {'form': form}
        return render(request, 'main/profile.html', context)


class ComparisonView(CategoryMixin, ListView):
    # Comparison product
    model = Product
    template_name = 'main/comparison.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comparison_ids = self.request.session.get('comparison_ids', [])
        comparison_products = Product.objects.filter(id__in=comparison_ids)
        context['comparison_products'] = comparison_products
        return context