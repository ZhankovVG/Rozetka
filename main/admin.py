from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class ImageAdminMixin():
    def get_image(self, object):
        return mark_safe(f"<img src={object.image.url} width='50' ")

    get_image.short_description = 'Фото'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Категории
    list_display = ('name', 'url', 'image')
    prepopulated_fields = {'url': ('name', )}
    list_display_links = ('name', )


class ReviewInline(admin.StackedInline):
    # Прикрипление отзывов к фильму
    model = Review
    readonly_fields = ('name', 'email')
    extra = 1


@admin.register(Salesman)
class SalesmanAdmin(ImageAdminMixin, admin.ModelAdmin):
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
    list_display = (
        'name', 
        'text', 
        'email', 
        'electronicsDevice',
        'hfridgeDevice',
        'washingDevice' 
        )
    list_display_links = ('name', )
    readonly_fields = ('name', 'email')


@admin.register(BrandElectronics)
class BrandElectronicsAdmin(ImageAdminMixin, admin.ModelAdmin):
    # марка электроники
    list_display = ('title', 'get_image')


@admin.register(ElectronicsDevice)
class ElectronicsDeviceAdmin(ImageAdminMixin, admin.ModelAdmin):
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
        'category',
        'draft',
        'code',
    )
    list_display_links = ('name', )
    inlines = [ReviewInline]
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
        'category',
        'draft',
        'code',
    )
    list_editable = ('draft',)
    search_fields = ('name', 'category__name')
    prepopulated_fields = {'url': ('name', )}


@admin.register(BrandHouseholdAppliances)
class BrandHouseholdAppliancesAdmin(ImageAdminMixin, admin.ModelAdmin):
    # марка бытовой техники 
    list_display = ('title', 'get_image')


@admin.register(Hfridge)
class HfridgeAdmin(ImageAdminMixin, admin.ModelAdmin):
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
        'draft',
        'code',
    )
    list_display_links = ('name', )
    inlines = [ReviewInline]
    list_filter = (
        'name',
        'series',
        'price',
        'fridge_capacity',
        'weight',
        'color',
        'brand',
        'category',
        'draft',
        'code',
    )
    list_editable = ('draft',)
    search_fields = ('name', 'category__name')
    prepopulated_fields = {'url': ('name', )}


@admin.register(WashingMachine)
class WashingMachineAdmin(ImageAdminMixin, admin.ModelAdmin):
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
        'draft',
        'code',
    )
    list_display_links = ('name', )
    inlines = [ReviewInline]
    list_filter = (
        'name',
        'price',
        'maximum_laundry_load',
        'color',
        'weight',
        'spin_speed',
        'brand',
        'category',
        'draft',
        'code',
    )
    list_editable = ('draft',)
    search_fields = ('name', 'category__name')
    prepopulated_fields = {'url': ('name', )}
