from django.shortcuts import render
import json


# Create your views here.
def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    with open('./mainapp/fixtures/products.json') as products_data:
        data = json.load(products_data)

    context = {
        'title': 'GeekShop - Каталог',
        'products': data,
    }
    return render(request, 'mainapp/products.html', context)

