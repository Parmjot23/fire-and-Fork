from django.urls import reverse
from rest_framework.test import APITestCase
from .models import MenuItem

class MenuItemTests(APITestCase):
    def test_list_menu(self):
        MenuItem.objects.create(name='Burger', price=9.99)
        url = reverse('menu-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
