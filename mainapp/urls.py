from django.urls import path
from mainapp.views import products

app_name = 'mainapp'
urlpatterns = [
    path('', products, name='p_index'),
    path('<int:id>/', products, name='product'),
]
