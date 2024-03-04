from rest_framework import viewsets

from products.models.category import ProductCategory
from products.models.product import Product
from products.serialziers import ProductCategorySerializer
from products.serialziers import ProductSerializer
from products.serialziers import ProductDetailsSerializer


class ProductCategoryView(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    http_method_names = ['get']


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']


class ProductDetailsView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    http_method_names = ['get']