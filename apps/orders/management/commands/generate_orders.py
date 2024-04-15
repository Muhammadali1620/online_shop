from typing import Any
from django.core.management import BaseCommand
from apps.orders.models import Order, OrderProduct
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        ordermodel = [Order(user_id=user.pk, 
                            payment_method_id=2,
                            payment_method_name=f'payment_method_name No {i}',
                            total_price=2000 * i,
                            delivery_price=1000 * i,
                            coupon_price=100 * i,
                            is_paid=True, 
                            first_name=f'first_name No {i}',
                            last_name=f'last_name No {i}',
                            phone_number='+998994337104',
                            address1=f'address1 No {i}',
                            address2=f'address2 No {i}',
                            country=f'country No {i}',
                            region=f'region No {i}',
                            district=f'district No {i}',
                        )
            for i in range(1, 6)
            for user in CustomUser.objects.all()
        ]
        Order.objects.bulk_create(ordermodel)
        self.stdout.write(self.style.SUCCESS('1000 ordermodel created'))

        orderproduct = [OrderProduct(product_feature_id=order.pk, counts=2, order_id=order.pk)
            for i in range(1, 6)
            for order in Order.objects.all()
        ]
        OrderProduct.objects.bulk_create(orderproduct)
        self.stdout.write(self.style.SUCCESS('1000 orderproduct created'))