from django.urls import path
from .import views

app_name = 'cabinet'

urlpatterns = [
    path('', views.PersonalCabinetView.as_view(), name='personal_cabinet'),
]