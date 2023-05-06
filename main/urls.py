from django.urls import path
from .import views


urlpatterns = [
    path('', views.ElectronicsDeviceViews.as_view(), name='main'),
    path('category/<slug:cat_slug>/', views.CategoryViews.as_view(), name='category')
]
