from django.contrib import admin

from products.models.category import ProductCategory
from products.models.product import Product

@admin.register(ProductCategory)
class UserAdminProductCategory(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class UserAdminProduct(admin.ModelAdmin):
    list_display = ('category', 'name', 'price')
