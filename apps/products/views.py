from django.shortcuts import get_object_or_404, render
from apps.features.models import Feature, FeatureValue, ProductFeature
from apps.products.models import Product
from apps.general.models import General
from apps.categories.models import MainCategory, SubCategory
from django.db.models import F


def product_list(request):
    categories = MainCategory.objects.all().order_by('?')[0:10]
    products = Product.objects.all().order_by('-pk')[0:9]
    features  = Feature.objects.all().order_by('ordering_number')[0:5]
    # annotate bu modelsda title yaratvotti va F "if" orqali "title_uz" yoki "title_ru" ligini aniqlavotti va titleni ichiga xar bir ichidi obyekkti qo'shib chiqvotti
    store_data = General.objects.first()
    context = {
        'categories':categories,
        'products':products, 
        'features':features,
        'store_data':store_data
    }
    return render(request, template_name='products/product_list.html', context=context)


def product_detail(request, pk):
    categories = MainCategory.objects.all().order_by('?')[0:10]
    store_data = General.objects.first()
    product = get_object_or_404(Product, pk=pk)
    products = Product.objects.all().order_by('?')[0:6]
    context = {
        'categories':categories,
        'store_data':store_data,
        'product':product,
        'products':products
    }
    return render(request, template_name='products/product_detail.html', context=context)