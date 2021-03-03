from django.shortcuts import render
import json
from mainapp.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    with open('mainapp/fixtures/products.json') as products_data:
        data = json.load(products_data)

    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)

