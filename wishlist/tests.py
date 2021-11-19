from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product
from .models import Wishlist

class TestWishlistViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpassword'
        )
        self.product = Product.objects.create(
            name='New Product',
            price='20.95',
            description='test description'
        )
        self.wishlist = reverse('wishlist')
        self.add_to_wishlist = reverse("add_to_wishlist",
                                       kwargs={"product_id": self.product.id})
        self.delete_wishlist_item = reverse("delete_wishlist_item",
                                            kwargs={"product_id": self.product.id})
    

    def test_get_wishlist_view(self):
        """
        A test to get the wishlist view
        """
        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.get(self.wishlist)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist/wishlist.html')
    

    def test_add_to_wishlist(self):
        """
        A test to test adding items to wishlist
        """
        self.client.login(
            username="testuser", password="testpassword")
        response = self.client.post(self.add_to_wishlist)
        wishlist = Wishlist.objects.get(user=self.user)
        products = wishlist.products.all()
        self.assertTrue(products[0], self.product)
    

    def test_delete_wishlist_item(self):
        """
        A test to test deleting items from a users wishlist
        """
        self.client.login(
            username="testuser", password="testpassword")
        self.client.post(self.add_to_wishlist)
        response = self.client.post(self.delete_wishlist_item)
        wishlist = Wishlist.objects.get(user=self.user)
        products = wishlist.products.all()
        self.assertFalse(products)