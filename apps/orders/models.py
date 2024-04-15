from django.db import models
from apps.features.models import ProductFeature
from apps.users.models import CustomUser
from apps.general.models import PaymentMethod
from apps.users.valedate import validate_phone_number
from django.core.validators import MinValueValidator, MaxValueValidator


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    payment_method_name = models.CharField(max_length=35, blank=True)
    total_price = models.FloatField(default=0)
    delivery_price = models.FloatField(default=0)
    coupon_price = models.FloatField(default=0)
    is_paid = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=13, validators=[validate_phone_number], blank=True)
    address1 = models.CharField(max_length=300, blank=True)
    address2 = models.CharField(max_length=300, blank=True)
    country = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=350, blank=True)
    zip_code = models.PositiveSmallIntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk}:{self.user}'


class OrderProduct(models.Model):
    product_feature = models.ForeignKey(ProductFeature, on_delete=models.PROTECT)
    counts = models.PositiveSmallIntegerField(default=1 ,validators=[MinValueValidator(1)])
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product_feature}'