from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Product, Review, Category


class ProductViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.category1 = Category.objects.create(name="Category1")
        self.product1 = Product.objects.create(name="Product1", category=self.category1, price=5000)
        self.product2 = Product.objects.create(name="Product2", category=self.category1, price=6000)
        self.review1 = Review.objects.create(product=self.product1, rating=5, user=self.user)
        self.review2 = Review.objects.create(product=self.product1, rating=4, user=self.user)
        self.client = APIClient()

    def test_list_products(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Paginated response has 'results' key
        self.assertEqual(len(response.data['results']), 2)

    def test_list_products_with_category_filter(self):
        response = self.client.get(reverse('product-list'), {'category': self.category1.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_retrieve_product(self):
        response = self.client.get(reverse('product-detail', args=[self.product1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('product', response.data)
        self.assertIn('related_products', response.data)

    def test_top_rated(self):
        # DRF uses hyphens for action names by default in recent versions
        response = self.client.get(reverse('product-top-rated'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_average_rating(self):
        response = self.client.get(reverse('product-average-rating', args=[self.product1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        avg_rating = (self.review1.rating + self.review2.rating) / 2
        self.assertEqual(response.data['average_rating'], avg_rating)
