from django.contrib import admin
from apps.orders.models import Order, OrderProduct


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_method', 'total_price', 'delivery_price', 'coupon_price', 'is_paid',
                    'email', 'phone_number',)
    readonly_fields = ('created_at',)

    list_display_linsk = ('user', 'payment_method', 'total_price', 'delivery_price', 'coupon_price', 'is_paid',
                    'email', 'phone_number',)
    list_filter = ['payment_method','is_paid']
    search_fields = ['user', 'total_price', 'delivery_price', 'coupon_price', 'email', 'phone_number']
    search_help_text = f'Serch from fields({search_fields})'


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('product_feature', 'counts', 'order')
    readonly_fields = ('created_at',)

    list_display_linsk = ('product_feature', 'order')
    list_filter = ['product_feature']
    search_fields = ['product_feature', 'counts', 'order']
    search_help_text = f'Serch from fields({search_fields})'
    list_editable = ['counts']