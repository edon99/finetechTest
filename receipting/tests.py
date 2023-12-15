from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Receipt



class ReceiptModelTest(TestCase):  #test class for models
    def setUp(self):    #set up any preconditions needed for test methods
        self.user = User.objects.create_user(username='testuser', password='testpassword') 

    def test_receipt_creation(self):  #creating test receipt
        receipt = Receipt.objects.create(
            store_name='Test Store',
            date='2023-01-01',
            item_list='Test item',
            total=10.0,
            user=self.user
        )

        self.assertEqual(receipt.store_name, 'Test Store')  #verify that the properties of the receipt object created match the expected values
        self.assertEqual(receipt.date, '2023-01-01')
        self.assertEqual(receipt.item_list, 'Test item')
        self.assertEqual(receipt.total, 10.0)
        self.assertEqual(receipt.user, self.user)

class ReceiptViewsTest(TestCase):   #tests for views
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')


        #under are same assertion tests to verify if function inputs and actual results do match or not

    def test_receipt_list_view(self):
        Receipt.objects.create(
            store_name='Test Store',
            date='2023-01-01',
            item_list='Test item',
            total=10.0,
            user=self.user
        )

        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('receipts'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Store')

    def test_receipt_create_view(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('new-receipt'), {
            'store_name': 'New Store',
            'date': '2023-01-02',
            'item_list': 'New item',
            'total': 15.0,
        })

        self.assertRedirects(response, reverse('receipts'))
        self.assertTrue(Receipt.objects.filter(store_name='New Store').exists())

    def test_receipt_details_view(self):
        receipt = Receipt.objects.create(
            store_name='Test Store',
            date='2023-01-01',
            item_list='Test item',
            total=10.0,
            user=self.user
        )

        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('details-receipt', args=[receipt.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Store')

    def test_receipt_update_view(self):
        receipt = Receipt.objects.create(
            store_name='Test Store',
            date='2023-01-01',
            item_list='Test item',
            total=10.0,
            user=self.user
        )

        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('update-receipt', args=[receipt.pk]), {
            'store_name': 'Updated Store',
            'date': '2023-01-03',
            'item_list': 'Updated item',
            'total': 20.0,
        })

        self.assertRedirects(response, reverse('receipts'))
        self.assertTrue(Receipt.objects.filter(store_name='Updated Store').exists()) #check if there is an object in the database where the store_name is Updated Store
