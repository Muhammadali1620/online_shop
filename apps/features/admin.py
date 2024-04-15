from django.contrib import admin
from apps.features.models import Feature, FeatureValue, ProductFeature


class FeatureValueInlineAdmin(admin.StackedInline):
    model = FeatureValue


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('main_category', 'sub_category', 'name_uz', 'name_ru')
    readonly_fields = ('created_at','updated_at',)
    prepopulated_fields = {'slug':['name_uz']}
    list_display_linsk = ('main_category', 'sub_category')
    list_filter = ['main_category','sub_category']
    search_fields = ['main_category', 'sub_category', 'name_uz', 'name_ru']
    search_help_text = f'Serch from fields({search_fields})'
    list_editable = ['name_uz', 'name_ru']
    inlines = [FeatureValueInlineAdmin]


@admin.register(FeatureValue)
class FeatureValueAdmin(admin.ModelAdmin):
    list_display = ('feature', 'value_uz', 'value_ru')
    readonly_fields = ('created_at','updated_at',)
    prepopulated_fields = {'slug':['value_uz']}

    list_display_linsk = ('feature')
    list_filter = ['feature']
    search_fields = ['name_uz','name_ru']
    search_help_text = f'Serch from fields({search_fields})'
    list_editable = ['value_uz', 'value_ru']


@admin.register(ProductFeature)
class ProductFeatureAdmin(admin.ModelAdmin):
    list_display = ('product', 'feature_value', 'quantity', 'price')
    readonly_fields = ('created_at',) 

    list_display_linsk = ('main_category', 'name_uz', 'name_ru')
    list_filter = ['product','feature_value']
    search_fields = ['product', 'feature_value', 'quantity']
    search_help_text = f'Serch from fields({search_fields})'
    list_editable = ['quantity', 'price']