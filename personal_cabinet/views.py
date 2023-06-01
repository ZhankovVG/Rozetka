from django.shortcuts import render
from django.views.generic import ListView
from .models import UserProfile


class PersonalCabinetView(ListView):
    model = UserProfile
    template_name = 'personal_cabinet/personal_cabinet.html'
