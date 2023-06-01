from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    orders  = models.CharField('Мои заказы', max_length=50, blank=True)
    wishlist = models.CharField('Cписок желаний', max_length=50, blank=True)
    browseed_items  = models.CharField('Просмотренные товары', max_length=50, blank=True)
    newsletters = models.CharField('Рассылки', max_length=50, blank=True)
    my_wallet = models.CharField('Мой кошелек', max_length=50, blank=True)
    my_reviews = models.CharField('Мои отзывы', max_length=50, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'