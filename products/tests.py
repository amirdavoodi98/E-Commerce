from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

from products.models.category import ProductCategory
from products.models.product import Product


class ProductCategoryTestCase(TestCase):
    fixtures = ['products_data_test']

    def setUp(self):
        self.client = APIClient()
        self.product_categories = ProductCategory.objects.all()
        self.products = Product.objects.all()

    def test_get_categories_list(self):
        response = self.client.get(reverse('categories_list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_categories_count = self.product_categories.count()
        product_category_first = self.product_categories.first()
        self.assertEqual(len(response.data), product_categories_count)
        self.assertEqual(response.data[0]['name'], product_category_first.name)
    
    def test_get_products_list(self):
        response = self.client.get(reverse('products_list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_count = self.products.count()
        self.assertEqual(len(response.data), product_count)
    
    def test_get_products_details(self):
        product_first = self.products.first()
        response = self.client.get(reverse('products_details', kwargs={'pk': product_first.id}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['name'], product_first.name)
        self.assertEqual(response.data['price'], product_first.price)
    


