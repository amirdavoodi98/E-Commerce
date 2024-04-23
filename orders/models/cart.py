from django.db import models

from users.models import User
from orders.enums.card_status import CardStatus


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='cards')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=CardStatus.choices(),
        default=CardStatus.OPEN.value,
    )

    @property
    def cart_total_price(self):
        orders = self.orders.all()
        return sum(order.total_price for order in orders)
