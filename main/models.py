from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=200)
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = 'name'


