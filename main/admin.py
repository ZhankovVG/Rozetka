from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class ImageAdmin():
    def get_image(self, object):
        return mark_safe(f"<img src={object.image.url} width='50' ")

    get_image.short_description = 'Фото'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin, ImageAdmin):
    # Категории
    list_display = ('name', 'url')
    prepopulated_fields = {'url': ('name', )}
    list_display_links = ('name', )


@admin.register(Salesman)
class SalesmanAdmin(admin.ModelAdmin, ImageAdmin):
    # Продавец
    list_display = ('name', 'get_image')
    list_display_links = ('name', )


@admin.register(RatingsStar)
class RatingStarAdmin(admin.ModelAdmin):
    # Звезда рейтинга
    list_display = ('value', )
    list_display_links = ('value', )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # Отзыв
    list_display = ('name', 'text', 'email')
    list_display_links = ('name', )
    readonly_fields = ('name', 'email')


@admin.register(BrandElectronics)
class BrandElectronicsAdmin(admin.ModelAdmin, ImageAdmin):
    # марка электроники
    list_display = ('title', 'get_image')


@admin.register(ElectronicsDevice)
class ElectronicsDeviceAdmin(admin.ModelAdmin, ImageAdmin):
    # Электроника
    list_display = (
        'name',
        'series',
        'price',
        'display_size',
        'main_camera',
        'battery_capacity',
        'CPU',
        'ram',
        'operating_system',
        'screen_refresh_rate',
        'ram_type',
        'ssd_capacity',
        'get_image',
        'brand',
        'category'
    )
    list_display_links = ('name', )
    list_filter = (
        'name',
        'series',
        'price',
        'display_size',
        'main_camera',
        'battery_capacity',
        'CPU',
        'ram',
        'operating_system',
        'screen_refresh_rate',
        'ram_type',
        'ssd_capacity',
        'category'
    )
    search_fields = ('name', 'category__name')


@admin.register(BrandHouseholdAppliances)
class BrandHouseholdAppliancesAdmin(admin.ModelAdmin, ImageAdmin):
    # марка бытовой техники холодильники
    list_display = ('title', 'get_image')


@admin.register(Hfridge)
class HfridgeAdmin(admin.ModelAdmin, ImageAdmin):
    # холодильник бытовая техника
    list_display = (
        'name',
        'series',
        'price',
        'fridge_capacity',
        'weight',
        'color',
        'get_image',
        'brand',
        'category',
    )
    list_display_links = ('name')
    list_filter = (
        'name',
        'series',
        'price',
        'fridge_capacity',
        'weight',
        'color',
        'brand',
        'category',
    )
    search_fields = ('name', 'category__name')


@admin.register(BrandWashingMachine)
class BrandWashingMachineAdmin(admin.ModelAdmin, ImageAdmin):
    # марка бытовой техники стиральные машинки
    list_display = ('title', 'get_image')


@admin.register(WashingMachine)
class WashingMachineAdmin(admin.ModelAdmin):
    # Стиральная машина бытовая техника
    list_display = (
        'name',
        'price',
        'maximum_laundry_load',
        'color',
        'weight',
        'spin_speed',
        'get_image',
        'brand',
        'category',
    )
    list_display_links = ('name', )
    list_filter = (
        'name',
        'price',
        'maximum_laundry_load',
        'color',
        'weight',
        'spin_speed',
        'brand',
        'category',
    )
    search_fields = ('name', 'category__name')
