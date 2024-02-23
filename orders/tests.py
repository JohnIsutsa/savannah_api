from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from orders.models import Order

User = get_user_model()

class OrderListAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass', email='testuser@example.com')
        self.client.force_authenticate(user=self.user)
        self.order = Order.objects.create(owner=self.user, amount=10, item='Paracetamol')
        self.url = reverse('order-list') 

    def test_list_orders(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_create_order(self):
        data = {'amount': 5, 'item': 'Paracetamol'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['amount'], data['amount'])
        self.assertEqual(response.data['item'], data['item'])

class OrderDetailAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass', email='testuser@example.com')
        self.client.force_authenticate(user=self.user)
        self.order = Order.objects.create(owner=self.user, amount=10, item='Paracetamol')
        self.url = reverse('order-detail', kwargs={'id': self.order.id}) 

    def test_retrieve_order(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.order.id)

    def test_update_order(self):
        data = {'amount': 20, 'item': 'Paracetamol'}
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['amount'], data['amount'])
        self.assertEqual(response.data['item'], data['item'])

    def test_delete_order(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Order.DoesNotExist):
            Order.objects.get(id=self.order.id)