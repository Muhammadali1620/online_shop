from django.shortcuts import render
from apps.categories.models import MainCategory
from apps.general.models import General
from apps.products.models import Product



def home(request): 
    store_data = General.objects.first()
    categories = MainCategory.objects.all().order_by('?')[0:12]
    featured_products =  Product.objects.all().order_by("?")[0:8]
    recent_products = Product.objects.all().order_by("?")[0:8]
    context = {
        'categories':categories,
        'store_data':store_data,
        'featured_products':featured_products,
        'recent_products':recent_products,
    }
    return render(request, template_name='index.html', context=context)