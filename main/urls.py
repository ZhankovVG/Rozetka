from django.urls import path
from .import views


urlpatterns = [
    path('', views.WashingMachineView.as_view(), name='main'),
    path('search/', views.SearchViews.as_view(), name='search'),
    path('<slug:slug>/', views.DetailProductView.as_view(), name='detail'),
]
