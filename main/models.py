from django.db import models


class Category(models.Model):
    # Category
    name = models.CharField('Название', max_length=200)
    image = models.ImageField('Иконки', upload_to='category_photo/')
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Salesman(models.Model):
    # Salesman
    name = models.CharField('Имя', max_length=50)
    image = models.ImageField('Иконка', upload_to='salesman/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'


class Product(models.Model):
    # all items
    name = models.CharField('Название', max_length=300)
    code = models.IntegerField('Код товара', blank=True, null=True)
    series = models.CharField('Серия', max_length=100)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    display_size = models.CharField('Размер дисплея', max_length=50)
    main_camera = models.CharField(
        'Основная камера', max_length=100, blank=True, null=True)
    fridge_capacity = models.PositiveSmallIntegerField(
        'Объем холодильной камеры, л', blank=True, null=True)
    weight = models.PositiveSmallIntegerField('Вес, кг', blank=True, null=True)
    color = models.CharField('Цвет', max_length=50, blank=True, null=True)
    maximum_laundry_load = models.CharField('Загрузка', max_length=50, blank=True, null=True)
    spin_speed = models.CharField('Скорость отжима', max_length=50, blank=True, null=True)
    battery_capacity = models.CharField('Ёмкость батареи', max_length=50)
    CPU = models.CharField('Процессор', max_length=50)
    ram = models.CharField('Оперативная память', max_length=50)
    operating_system = models.CharField('Операционная система', max_length=50)
    screen_refresh_rate = models.CharField(
        'Частота обновления экрана', max_length=30, blank=True, null=True)
    ram_type = models.CharField(
        'Тип оперативной памяти', max_length=20, blank=True, null=True)
    ssd_capacity = models.CharField(
        'Объём SSD', max_length=20, blank=True, null=True)
    image = models.ImageField('Фото', upload_to='MobileTvTabletDevice/')
    url = models.SlugField(max_length=200, unique=True, default='')
    draft = models.BooleanField('Черновик', default=False)
    by_action = models.BooleanField('Акциооный товар', default=False) 
    brand_1 = models.ForeignKey(
        'BrandElectronics', on_delete=models.CASCADE, verbose_name='Марка')
    brand_2 = models.ForeignKey(
        'BrandHouseholdAppliances', on_delete=models.CASCADE, verbose_name='Марка')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f"{self.brand_1} {self.brand_2} {self.name}"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']


class BrandHouseholdAppliances(models.Model):
    # Household brand
    title = models.CharField('Название', max_length=100)
    image = models.ImageField(upload_to='brand_HouseholdAppliances_images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Марка бытовой техники'
        verbose_name_plural = 'Марки бытовой техники'


class BrandElectronics(models.Model):
    # Electronics brand
    title = models.CharField('Название', max_length=100)
    image = models.ImageField(upload_to='brand_Electronics_images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Марка электроники'
        verbose_name_plural = 'Марки электроники'


class RatingsStar(models.Model):
    # Star Rating
    value = models.PositiveSmallIntegerField('Значение', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'
        ordering = ['-value']


class Rating(models.Model):
    # Rating
    ip = models.CharField('IP адресс', max_length=60)
    star = models.ForeignKey(
        RatingsStar, on_delete=models.CASCADE, verbose_name='Звезда')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Товар')
    
    def __str__(self):
        return self.star

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
    

class Review(models.Model):
    # Review
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Коментарий', max_length=5000)
    email = models.EmailField()
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Родитель'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Товар')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'