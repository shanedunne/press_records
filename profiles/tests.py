from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile
from checkout.models import Order

class TestUserProfileViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpassword'
        )
        self.profile = reverse('profile')
    

    def test_get_profile_view(self):
        """
        A test to get the profile view
        """
        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.get(self.profile)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
    

    def test_get_order_history(self):
        """
        A test to get the order history on the profile page
        """
        self.client.login(
            username="testuser", password="testpassword")
        user_profile = UserProfile.objects.get(user=self.user)
        order = Order.objects.create(user_profile=user_profile)
        response = self.client.get(reverse('order_history', 
                                    kwargs={"order_number": order.order_number}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
