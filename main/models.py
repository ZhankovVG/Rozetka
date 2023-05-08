from django.db import models


class Category(models.Model):
    # Категория
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
    star = models.ForeignKey(
        RatingsStar, on_delete=models.CASCADE, verbose_name='Звезда')
    electronicsDevice = models.ForeignKey(
        'ElectronicsDevice', on_delete=models.CASCADE, verbose_name='Товар электоники')
    hfridgeDevice = models.ForeignKey(
        'Hfridge', on_delete=models.CASCADE, verbose_name='Товар холодильники')
    washingDevice = models.ForeignKey(
        'WashingMachine', on_delete=models.CASCADE, verbose_name='Товар стиральные машинки')
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
    electronicsDevice = models.ForeignKey(
        'ElectronicsDevice', on_delete=models.CASCADE, verbose_name='Товар электоники')
    hfridgeDevice = models.ForeignKey(
        'Hfridge', on_delete=models.CASCADE, verbose_name='Товар холодильники')
    washingDevice = models.ForeignKey(
        'WashingMachine', on_delete=models.CASCADE, verbose_name='Товар стиральные машинки')
    # не забыть подключить к каждому товару

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class BrandElectronics(models.Model):
    # марка электроники
    title = models.CharField('Название', max_length=100)
    image = models.ImageField(upload_to='brand_Electronics_images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Марка электроники'
        verbose_name_plural = 'Марки электроники'


class ElectronicsDevice(models.Model):
    # Электроника
    name = models.CharField('Название', max_length=300)
    code = models.IntegerField('Код товара', blank=True, null=True)
    series = models.CharField('Серия', max_length=100)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    display_size = models.CharField('Размер дисплея', max_length=50)
    main_camera = models.CharField(
        'Основная камера', max_length=100, blank=True, null=True)
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
    brand = models.ForeignKey(
        BrandElectronics, on_delete=models.CASCADE, verbose_name='Марка')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f"{self.brand} {self.name}"

    class Meta:
        verbose_name = 'Электроника'
        verbose_name_plural = 'Электроника'
        ordering = ['name']


class BrandHouseholdAppliances(models.Model):
    # марка бытовой техники холодильники
    title = models.CharField('Название', max_length=100)
    image = models.ImageField(upload_to='brand_HouseholdAppliances_images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Марка бытовой техники холодильники'
        verbose_name_plural = 'Марки бытовой техники холодильники'


class Hfridge(models.Model):
    # холодильник бытовая техника
    name = models.CharField('Название', max_length=300)
    code = models.IntegerField('Код товара', blank=True, null=True)
    series = models.CharField('Серия', max_length=100)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    fridge_capacity = models.PositiveSmallIntegerField(
        'Объем холодильной камеры, л')
    weight = models.PositiveSmallIntegerField('Вес, кг')
    color = models.CharField('Цвет', max_length=50)
    image = models.ImageField('Изображение', upload_to='hfridge/')
    url = models.SlugField(max_length=200, unique=True, default='')
    draft = models.BooleanField('Черновик', default=False)
    by_action = models.BooleanField('Акциооный товар', default=False)   
    brand = models.ForeignKey(BrandHouseholdAppliances,
                              on_delete=models.CASCADE, verbose_name='Марка')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Холодильник'
        verbose_name_plural = 'Холодильники'
        ordering = ['name']


class BrandWashingMachine(models.Model):
    # марка бытовой техники стиральные машинки
    title = models.CharField('Название', max_length=100)
    image = models.ImageField(upload_to='brand_WashingMachine_images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Марка стиральные машинки'
        verbose_name_plural = 'Марки стиральные машинки'


class WashingMachine(models.Model):
    # Стиральная машина бытовая техника
    name = models.CharField('Название', max_length=300)
    code = models.IntegerField('Код товара', blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    maximum_laundry_load = models.CharField('Загрузка', max_length=50)
    color = models.CharField('Цвет', max_length=20)
    weight = models.PositiveSmallIntegerField('Вес, кг')
    spin_speed = models.CharField('Скорость отжима', max_length=50)
    image = models.ImageField('Фото', upload_to='washing_machines/')
    url = models.SlugField(max_length=200, unique=True, default='')
    draft = models.BooleanField('Черновик', default=False)
    by_action = models.BooleanField('Акциооный товар', default=False) 
    brand = models.ForeignKey(BrandHouseholdAppliances,
                              on_delete=models.CASCADE, verbose_name='Марка')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стиральная машина'
        verbose_name_plural = 'Стиральные машинки'
