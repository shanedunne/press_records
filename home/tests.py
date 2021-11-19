from django.test import TestCase
from django.urls import reverse

class TestHomePage(TestCase):

    def setUp(self):

        self.home = reverse('home')
    

    def test_homepage_view(self):
        """
        A test to test the home page is returned
        """
        response = self.client.get(self.home)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')