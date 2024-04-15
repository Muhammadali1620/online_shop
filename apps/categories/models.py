from django.db import models
from apps.general.servises import normalize_text
from django.utils.translation import get_language


class MainCategory(models.Model):
    name_uz = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='category/image/', blank=True, null=True)
    product_counts = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def get_title(self):
        return getattr(self, f'name_{get_language()}')

    def get_normalize_fields(self):
        return ['name_uz', 'name_ru']
    
    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_uz
    

class SubCategory(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE,  related_name='sub_cat')
    name_uz = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_title(self):
        return getattr(self, f'name_{get_language()}')

    def __str__(self):
        return f'{self.main_category}:{self.name_uz}'
    
    def get_normalize_fields(self):
        return ['name_uz', 'name_ru']
    
    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)
