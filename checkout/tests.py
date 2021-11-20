from django.test import TestCase
from django.urls import reverse
from products.models import Product
from django.contrib.auth.models import User


class TestCheckoutViews(TestCase):

    def setUp(self):
        self.checkout = reverse('checkout')
        self.product = Product.objects.create(
            name='New Product',
            price='20.95',
            description='test description'
        )
        self.add_to_bag = reverse("add_to_bag",
                                  kwargs={"item_id": self.product.id})

    def test_checkout_view(self):
        self.client.post(self.add_to_bag,
                         data={'quantity': '1',
                               'redirect_url': '/'})
        response = self.client.get(self.checkout)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout.html")

    def test_checkout_success_view(self):
        self.client.post(self.add_to_bag,
                         data={'quantity': '1',
                               'redirect_url': '/'})
        response = self.client.post(self.checkout,
                                    data={
                                        'full_name': 'Test Name',
                                        'email': 'test@test.com',
                                        'phone_number': '123456789',
                                        'country': 'IE',
                                        'postcode': '12345',
                                        'town_or_city': 'Test City',
                                        'street_address1': 'Test St',
                                        'street_address2': '',
                                        'county': 'Test County',
                                        'client_secret': 'client',
                                    }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout_success.html")
