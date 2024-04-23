from rest_framework import serializers

from .models.cart import Cart
from .models.order import Order
from products.models.product import Product
from orders.validator_errors import NotStockError


class OrderSerialzier(serializers.ModelSerializer):
    total_price = serializers.FloatField(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'product', 'amount', 'total_price')
        read_only_fields = ('id', 'total_price')

    def validate(self, attrs):
        product: Product = attrs['product']
        if product.is_stock(amount=attrs['amount']):
            raise NotStockError(
                detail={'stock': f"not enough stock on {product.name}"})
        return super().validate(attrs)


class CartCreateSerializer(serializers.ModelSerializer):
    orders = OrderSerialzier(many=True)

    class Meta:
        model = Cart
        fields = ('id', 'orders', 'comment', 'status',
                  'cart_total_price', 'created_at')
        read_only_fields = ('id', 'status', 'cart_total_price', 'created_at')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        orders = validated_data.pop('orders')
        cart = Cart.objects.create(**validated_data)
        for order in orders:
            Order.objects.create(cart=cart, **order)
        return cart
