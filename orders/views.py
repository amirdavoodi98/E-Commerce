from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from orders.models.cart import Cart
from .serializers import CartCreateSerializer


class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartCreateSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']