from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Reservation
from django.utils import timezone

class ReservationTests(APITestCase):
    def test_create_reservation(self):
        url = reverse('reservations-list')
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'pax': 2,
            'datetime': timezone.now().isoformat()
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Reservation.objects.count(), 1)
