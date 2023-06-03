from django.urls import path
from .import views


app_name = 'personal_cabinet'

urlpatterns = [
    path('', views.PersonalCabinetView.as_view(), name='cabinet'),
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('wishlist/', views.WishlistView.as_view(), name='wish_list'),
]