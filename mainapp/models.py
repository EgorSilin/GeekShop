from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return f'{self.id}. {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=128, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images', blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}. {self.name} ({self.category.name})'
