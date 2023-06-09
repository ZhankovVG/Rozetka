from django.urls import path
from .import views


urlpatterns = [
    path('', views.WashingMachineView.as_view(), name='main'),
    path('search/', views.SearchViews.as_view(), name='search'),
    path('product/<slug:slug>/', views.DetailProductView.as_view(), name='detail'),
    path('category/<slug:cat_slug>/', views.CategoryOutputView.as_view(), name='category'),
    path('brand/<slug:brand_slug>/', views.BrandOutputView.as_view(), name='brand'),
    path('review/<int:pk>/', views.ReviewsView.as_view(), name='review'),
    path('add-rating/', views.AddStarsRating.as_view(), name='add_rating'),
    path('profile/', views.PersonalCabinetView.as_view(), name='profile'),
    path('compare/', views.CompareView.as_view(), name='compare'),

]
