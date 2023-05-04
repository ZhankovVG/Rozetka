from django.urls import path
from .import views


urlpatterns = [
    path('', views.ElectronicsDeviceViews.as_view(), name='main'),
]
