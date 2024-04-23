from django.db import models

from products.models.product import Product
from orders.models.cart import Cart


class Order(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='orders')
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='orders')
    amount = models.IntegerField(default=1)

    @property
    def total_price(self):
        return self.amount * self.product.price
    
    @property
    def status(self):
        return self.cart.status
