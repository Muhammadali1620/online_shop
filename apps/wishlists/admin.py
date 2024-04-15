from django.contrib import admin
from apps.wishlists.models import Wishlist


@admin.register(Wishlist) 
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    readonly_fields = ('created_at',)

    list_display_linsk = ('user', 'product', 'created_at')
    search_fields = ['user', 'product']
    search_help_text = f'Serch from fields({search_fields})'
