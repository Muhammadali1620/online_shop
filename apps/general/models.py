from django.db import models
from django.core.exceptions import ValidationError
from apps.general.servises import normalize_text
from apps.users.valedate import validate_phone_number
from apps.categories.models import SubCategory
from django.utils.translation import get_language


class SocialLink(models.Model):
    icon = models.ImageField(upload_to='general/social_link/icon/', blank=True, null=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    link = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_normalize_fields(self):
        return ['name']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)


class PaymentMethod(models.Model):
    name = models.CharField(max_length=35)
    slug = models.SlugField(max_length=35, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_normalize_fields(self):
        return ['name']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)


class General(models.Model):
    delivery_price = models.FloatField(default=0)
    stor_name = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='general/logotype/image/')
    phone_number = models.CharField(max_length=13, validators=[validate_phone_number])
    email = models.EmailField() 
    address_uz = models.CharField(max_length=100)
    address_ru = models.CharField(max_length=100, blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    desc_uz = models.TextField(max_length=1000)
    desc_ru = models.TextField(max_length=1000, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_address(self):
        return getattr(self, f'address_{get_language()}')
    
    def get_desc(self):
        return getattr(self, f'desc_{get_language()}')

    def get_normalize_fields(self):
        return ['stor_name', 'address_uz', 'address_ru', 'desc_uz', 'desc_ru']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)


class Service(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='general/service/icon/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_normalize_fields(self):
        return ['title_uz', 'title_ru']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_uz


class Branch(models.Model):
    image = models.FileField(upload_to='general/image', blank=True, null=True)
    title_uz = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    title_ru = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_normalize_fields(self):
        return ['title_uz', 'title_ru']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_uz


class Banner(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    title_uz = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    title_ru = models.CharField(max_length=100, blank=True)
    desc_uz = models.CharField(max_length=500)
    desc_ru = models.CharField(max_length=500, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_normalize_fields(self):
        return ['title_uz', 'title_ru', 'desc_uz', 'desc_ru']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_uz


class Coupon(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=6, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="So'mda yoki foizda kiriting!!!")
    amount_is_percent = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_normalize_fields(self):
        return ['title', 'code']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def clean(self):
        if self.amount_is_percent and not (1 <= self.amount <= 100):
            raise ValidationError({'ammaut':'Invalid ammount [1- 100]'})

    def __str__(self):
        return self.title
