from django.shortcuts import render
import json
from mainapp.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request, id=None):
    context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all(),
    }
    context.update(
        {
            'products': Product.objects.filter(category_id=id) if id else Product.objects.all()
        }
    )
    return render(request, 'mainapp/products.html', context)
