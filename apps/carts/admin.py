from django.contrib import admin
from apps.carts.models import Cart


@admin.register(Cart) 
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'ProductFeature', 'counts')
    list_display_linsk = ('user', 'ProductFeature', 'counts')
    search_fields = ['user', 'ProductFeature', 'counts']
    search_help_text = f'Serch from fields({search_fields})'
