from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Salesman)
class ActorTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(BrandProduct)
class GenreTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Product)
class MovieTranslationOptions(TranslationOptions):
    fields = ('name', 'display_size',
        )


@register(Review)
class MovieShotsTranslationOptions(TranslationOptions):
    fields = ('name', 'text')
