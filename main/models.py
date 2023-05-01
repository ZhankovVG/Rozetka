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


class Salesman(models.Model):
    # Продавец
    name = models.CharField('Имя', max_length=50)
    image = models.ImageField('Иконка', upload_to='salesman/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'


class RatingsStar(models.Model):
    # Звезда рейтинга
    value = models.PositiveSmallIntegerField('Значение', default=0)

    def __str__(self):
        return f'{self.value}'
    
    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'
        ordering = ['-value']


class Rating(models.Model):
    # Рейтинг
    ip = models.CharField('IP адресс', max_length=60)
    star = models.ForeignKey(RatingsStar, on_delete=models.CASCADE, verbose_name='Звезда')
    # не забыть подключить к каждому товару

    def __str__(self):
        return self.star
    
    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Review(models.Model):
    # Отзыв
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Коментарий', max_length=5000)
    email = models.EmailField()
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Родитель'
    )
    # не забыть подключить к каждому товару

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Brand(models.Model):
    # марка
    title = models.CharField('Название', max_length=100)
    image = models.ImageField(upload_to='brand_images/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'
        ordering = 'title'


class MobileDevice(models.Model):
    # Мобильные телефоны
    model = models.CharField('Название', max_length='100')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    display_size = models.CharField('Размер дисплея', max_length=50)
    processor = models.CharField('Процессор', max_length=100)
    main_camera = models.CharField('Основная камера', max_length=100)
    battery_capacity = models.CharField(max_length=50)
    CPU = models.CharField('Процессор',max_length=50)
    ram = models.CharField('Оперативная память', max_length=50)
    operating_system = models.CharField('Операционная система', max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.model}"
    
    class Meta:
        verbose_name = 'Мобильный телефон'
        verbose_name_plural = 'Мобильные телефоны'
        ordering = 'model'