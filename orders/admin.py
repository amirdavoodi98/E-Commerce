from django.contrib import admin

from orders.models.cart import Cart
from orders.models.order import Order


@admin.register(Cart)
class UserAdminCart(admin.ModelAdmin):
    list_display = ('id', 'user', 'comment', 'cart_total_price')


@admin.register(Order)
class UserAdminOrder(admin.ModelAdmin):
    list_display = ('id', 'product', 'amount', 'total_price', 'cart', 'status')
