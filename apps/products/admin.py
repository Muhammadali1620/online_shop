from django.contrib import admin
from apps.products.models import Product, ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title_uz', 'title_ru', 'price', 'old_price', 'rating')
    readonly_fields = ('created_at','updated_at','rating','review_counts')
    prepopulated_fields = {'slug':['title_uz']}

    list_display_linsk = ('slug')
    list_filter = ['rating']
    search_fields = ['title_uz', 'title_ru', 'price', 'old_price', 'review_counts']
    search_help_text = f'Serch from fields({search_fields})'
    list_editable = ['title_uz', 'title_ru', 'price', 'old_price']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display_linsk = ('product')