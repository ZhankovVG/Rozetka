from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Salesman)
class SalesmanTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(BrandProduct)
class BrandProductTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'code',
        'series',
        'price',
        'display_size',
        'main_camera',
        'fridge_capacity',
        'weight',
        'color',
        'maximum_laundry_load',
        'spin_speed',
        'battery_capacity',
        'CPU',
        'ram',
        'operating_system',
        'screen_refresh_rate',
        'ram_type',
        'ssd_capacity',
    )
