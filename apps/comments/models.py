from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.users.models import CustomUser
from apps.products.models import Product
from apps.general.servises import normalize_text


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    message = models.CharField(max_length=300)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_normalize_fields(self):
        return ['name', 'message']
    
    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)
 
    def __str__(self):
        return f'{self.name}:{self.message}'
