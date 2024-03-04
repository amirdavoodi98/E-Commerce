from django.urls import path

from products.views import ProductCategoryView, ProductDetailsView, ProductView

urlpatterns = [
    path('category/', ProductCategoryView.as_view({
        'get': 'list'
    }), name='categories_list'),
    path('products/', ProductView.as_view({
        'get': 'list',
    }), name='products_list'),
    path('products/<int:pk>', ProductDetailsView.as_view({
        'get': 'retrieve',
    }), name='products_details'),
    
]