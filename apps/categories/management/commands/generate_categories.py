from typing import Any
from django.core.management import BaseCommand
from apps.categories.models import MainCategory, SubCategory
 

class Command(BaseCommand):
    def handle(self, *args, **options):
        last = MainCategory.objects.all().order_by('-pk').first()
        maincategory = [MainCategory(name_uz = f'Main category NO {i}', 
                         name_ru=f'Main category NO {i}. ru', 
                         slug=f'main-category-no-{i}')
            for i in range(last.pk + 1 if last else 1, last.pk + 1002 if last else 1001)
        ]
        MainCategory.objects.bulk_create(maincategory)
        self.stdout.write(self.style.SUCCESS('1000 maincategory created')) 

        subcategory = [SubCategory(main_category_id=main.pk, 
                        name_uz=f'Sub category NO {i}', 
                        name_ru = f'Sub category NO {i}. ru', 
                        slug = f'sub-category-{main}-no-{i}')
            for i in range(1, 6)
            for main in MainCategory.objects.all()
        ]
        SubCategory.objects.bulk_create(subcategory)
        self.stdout.write(self.style.SUCCESS('1000 subcategory created')) 