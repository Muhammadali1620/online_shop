from typing import Any
from django.core.management import BaseCommand
from apps.categories.models import SubCategory
from apps.general.models import SocialLink, PaymentMethod, Service, Banner, Branch, Coupon


class Command(BaseCommand):
    def handle(self, *args, **options): 
        last = SocialLink.objects.all().order_by('-pk').first()
        sociallink = [SocialLink(name=f'name No {i}', 
                                 slug=f'slug-no-{i}', 
                                 link=f'https://www.google.com/{i}')
            for i in range(last.pk + 1 if last else 1, last.pk + 7 if last else 6)
        ]
        SocialLink.objects.bulk_create(sociallink)
        self.stdout.write(self.style.SUCCESS('5 sociallink created'))

        last = PaymentMethod.objects.all().order_by('-pk').first()
        paymentmethod = [PaymentMethod(name=f'name No {i}', slug=f'slug-no-{i}')
            for i in range(last.pk + 1 if last else 1, last.pk + 6 if last else 7)
        ]
        PaymentMethod.objects.bulk_create(paymentmethod)
        self.stdout.write(self.style.SUCCESS('5 paymentmethod created'))

        last = Service.objects.all().order_by('-pk').first()
        servises = [
            Service(title_uz=f'title_uz No {i}', slug=f'slug-no-{i}', title_ru=f'title_ru No {i}')
            for i in range(last.pk + 1 if last else 1, last.pk + 7 if last else 6)
        ]
        Service.objects.bulk_create(servises)
        self.stdout.write(self.style.SUCCESS('5 servises created'))

        banner = [
            Banner(sub_category_id=sub_category.pk, slug=f'slug-no-{i}', title_uz=f'title_uz No {i}', title_ru=f'title_uz No {i}', desc_uz=f'desc_uz No {i}', desc_ru=f'desc_ru No {i}')
            for i in range(1, 6)
            for sub_category in SubCategory.objects.all()
        ]
        Banner.objects.bulk_create(banner)
        self.stdout.write(self.style.SUCCESS('5 banner created'))

        last = Branch.objects.all().order_by('-pk').first()
        branch = [
            Branch(title_uz=f'title_uz No {i}', slug=f'slug-no-{i}', title_ru=f'title_ru No {i}')
            for i in range(last.pk + 1 if last else 1, last.pk + 7 if last else 6)
        ]
        Branch.objects.bulk_create(branch)
        self.stdout.write(self.style.SUCCESS('5 branch created'))

        last = Coupon.objects.all().order_by('-pk').first()
        cupon = [
            Coupon(title=f'title No {i}', code=f'code No {i}', amount='50')
            for i in range(last.pk + 1 if last else 1, last.pk + 7 if last else 6)
        ]
        Coupon.objects.bulk_create(cupon)
        self.stdout.write(self.style.SUCCESS('5 cupon created'))