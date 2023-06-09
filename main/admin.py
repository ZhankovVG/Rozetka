from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
from main.models import UserProfile



class ImageAdminMixin():
    def get_image(self, object):
        return mark_safe(f"<img src={object.image.url} width='50' ")

    get_image.short_description = 'Фото'


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    # Category
    list_display = ('name', 'url', 'image')
    prepopulated_fields = {'url': ('name', )}
    list_display_links = ('name', )


class ReviewInline(admin.StackedInline):
    # Attaching movie reviews
    model = Review
    readonly_fields = ('name', 'email')
    extra = 1


@admin.register(Salesman)
class SalesmanAdmin(ImageAdminMixin, TranslationAdmin):
    # Salesman
    list_display = ('name', 'get_image')
    list_display_links = ('name', )


@admin.register(RatingsStar)
class RatingStarAdmin(admin.ModelAdmin):
    # Star rating
    list_display = ('value', )
    list_display_links = ('value', )


@admin.register(Rating)
# Star
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('star', 'product', 'ip')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # Review
    list_display = (
        'name', 
        'text', 
        'email', 
        'product',
        )
    list_display_links = ('name', )
    readonly_fields = ('name', 'email')


@admin.register(BrandProduct)
class BrandAdmin(ImageAdminMixin, TranslationAdmin):
    # brand of electronics
    list_display = ('title', 'get_image')
    prepopulated_fields = {'url': ('title', )}


@admin.register(Product)
class ProductAdmin(ImageAdminMixin, TranslationAdmin):
    # Product
    list_display = (
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
        'get_image',
        'brand',
        'category',
        'draft',
        'by_action',
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
        'brand',
        'draft',
        'by_action',
    )
    list_editable = ('draft', 'by_action')
    search_fields = ('name', 'category__name')
    prepopulated_fields = {'url': ('name', )}


admin.site.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'profile_image')
    readonly_fields = ('phone',)
    list_filter = ('first_name',)