from django.db import models
from django.core.validators import MinValueValidator

from .category import ProductCategory


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.FloatField(validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['name']

    @property
    def category_name(self):
        return self.category.name

    def __str__(self):
        return self.name
    
    def increase_stock(self, amount: int):
        if amount <= 1:
            raise ValueError("Amount must be a positive integer and greater than 0")
        
        self.stock = self.stock + amount
        self.save()

    def decrease_stock(self, amount: int):
        if amount <= 1:
            raise ValueError("Amount must be a positive integer and greater than 0")
        
        self.stock = self.stock - amount
        self.save()