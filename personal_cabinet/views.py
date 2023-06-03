from django.shortcuts import render
from django.views.generic import ListView
from .models import UserProfile


class PersonalCabinetView(ListView):
    model = UserProfile
    context_object_name = 'user_profile'

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)
    

class OrderListView(ListView):
    model = UserProfile
    template_name = 'personal_cabinet/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        user_profile = self.request.user.userprofile
        return user_profile.orders
    

class WishlistView(ListView):
    model = UserProfile
    template_name = 'personal_cabinet/wish_list.html'
    context_object_name = 'wishlist_items'

    def get_queryset(self):
        user_profile = self.request.user.userprofile
        return user_profile.wishlist
    
