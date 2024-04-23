import django_filters

from products.models.product import Product


class ProductFilter(django_filters.FilterSet):
    gte_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    lte_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['category', 'gte_price', 'lte_price']
