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
        'main_camera',
        'color',
        'CPU',
        'ram',
        'operating_system',
        'screen_refresh_rate',
        'ram_type',
        'ssd_capacity',
    )
