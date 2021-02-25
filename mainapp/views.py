from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': [
            {
                "id": "1",
                "picture": "vendor/img/products/Adidas-hoodie.png",
                "name": "Худи черного цвета с монограммами adidas Originals",
                "price": "6 090,00",
                "text": "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни."
            },
            {
                "id": "2",
                "picture": "vendor/img/products/Blue-jacket-The-North-Face.png",
                "name": "Синяя куртка The North Face",
                "price": "23 725,00",
                "text": "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель."
            },
            {
                "id": "3",
                "picture": "vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png",
                "name": "Коричневый спортивный oversized-топ ASOS DESIGN",
                "price": "3 390,00",
                "text": "Материал с плюшевой текстурой. Удобный и мягкий."
            },
            {
                "id": "4",
                "picture": "vendor/img/products/Black-Nike-Heritage-backpack.png",
                "name": "Черный рюкзак Nike Heritage",
                "price": "2 340,00",
                "text": "Плотная ткань. Легкий материал."
            },
            {
                "id": "5",
                "picture": "vendor/img/products/Black-Dr-Martens-shoes.png",
                "name": "Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex",
                "price": "13 590,00",
                "text": "Гладкий кожаный верх. Натуральный материал."
            },
            {
                "id": "6",
                "picture": "vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png",
                "name": "Темно-синие широкие строгие брюки ASOS DESIGN",
                "price": "2 890,00",
                "text": "Легкая эластичная ткань сирсакер Фактурная ткань."
            }
        ],
    }
    return render(request, 'mainapp/products.html', context)


def test_context(request):
    context = {
        'title': 'geekshop',
        'header': 'Добро пожаловать на сайт!',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00'},
        ],
        'promotion': True,
        'products_of_promotion': [
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00'},
        ],
    }
    return render(request, 'mainapp/test_context.html', context)
