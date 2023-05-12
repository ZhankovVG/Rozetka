from django.urls import path
from .import views


urlpatterns = [
    path('', views.HouseholdAppliancesView.as_view(), name='main'),
    path('search/', views.SearchViews.as_view(), name='search')
]
