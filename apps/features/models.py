from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from apps.general.servises import normalize_text
from apps.products.models import Product
from apps.categories.models import MainCategory, SubCategory


class Feature(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.PROTECT,
                                        blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT,
                                        blank=True, null=True)
    ordering_number = models.PositiveSmallIntegerField(unique=True)
    name_uz = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    name_ru = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_normalize_fields(self):
        return ['name_uz', 'name_ru']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def get_category(self):
        return self.main_category or self.sub_category

    def clean(self):
        if self.main_category and self.sub_category or   not self.main_category and not self.sub_category:
            raise ValidationError('Bitta Category ni tanla')

    def __str__(self):
        return self.name_uz


class FeatureValue(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='values')
    value_uz = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)
    value_ru = models.CharField(max_length=30, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_normalize_fields(self):
        return ['value_uz', 'value_ru']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.value_uz

    class Meta:
        unique_together = ('feature', 'value_uz')


class ProductFeature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    feature_value = models.ForeignKey(FeatureValue, on_delete=models.CASCADE, related_name='features')
    quantity = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product}'
    
    def clean(self):
        if self.feature_value.feature.get_category() not in [self.product.main_category,
                                                             self.product.sub_category] + list(self.product.main_category.subcategorymodel_set.all):
            raise ValidationError({'feature_value':'Feature category not equal to product category'})

    class Meta:
        unique_together = ('product', 'feature_value')
