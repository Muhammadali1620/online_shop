from typing import Any
from django.core.management import BaseCommand
from apps.products.models import Product, ProductImage


class Command(BaseCommand):
    def handle(self, *args, **options):
        last = Product.objects.all().order_by('-pk').first()
        product = [Product(main_category_id=i if i % 2 == 0 else None, 
                           sub_category_id=i if i % 2 != 0 else None, 
                           title_uz=f'title_uz No {i}',
                           title_ru=f'title_ru No {i}',
                           slug=f'slug-no-{i}',
                           price=200000,
                           old_price=200000,
                           short_desc_uz=f'short_desc_uz No {i}',
                           short_desc_ru=f'short_desc_ru No {i}',
                           long_desc_uz=f'long_desc_uz No {i}',
                           long_desc_ru=f'long_desc_ru No {i}',)
            for i in range(last.pk + 1 if last else 1, last.pk + 1002 if last else 1001)
        ]
        Product.objects.bulk_create(product)
        self.stdout.write(self.style.SUCCESS('1000 product created'))

#        productimage = [
#            ProductImage(product_id={i})
#            for i in range(1, 1001)
#        ]
#        Product.objects.bulk_create(productimage)
#        self.stdout.write(self.style.SUCCESS('1000 productimage created'))