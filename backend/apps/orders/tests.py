from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Order

class OrderTests(APITestCase):
    def test_create_order(self):
        url = reverse('orders-list')
        response = self.client.post(url, {'total': '10.00'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Order.objects.count(), 1)
