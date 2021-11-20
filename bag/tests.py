from django.test import TestCase
from products.models import Product
from django.contrib.auth.models import User
from django.urls import reverse


class TestBagViews(TestCase):

    def setUp(self):
        """
        Set up requirements for view testing
        """

        self.product = Product.objects.create(
            name='New Product',
            price='20.95',
            description='test description'
        )
        self.view_bag = reverse("view_bag")
        self.add_to_bag = reverse('add_to_bag',
                                  kwargs={"item_id": self.product.id})
        self.adjust_bag = reverse("adjust_bag",
                                  kwargs={"item_id": self.product.id})
        self.remove_from_bag = reverse("remove_from_bag",
                                       kwargs={"item_id": self.product.id})

    def test_get_bag_view(self):
        """
        A test to get the bag view
        """
        response = self.client.get(self.view_bag)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_to_add_to_bag(self):
        """
        A test to add product to a bag
        """

        response = self.client.post(self.add_to_bag, data={'quantity': '1',
                                    'redirect_url': '/'})
        response = self.client.post(self.view_bag)
        context = response.context
        self.assertNotEqual(context["bag_items"], [])
        self.assertEqual(context["bag_items"][0]["item_id"],
                         f"{self.product.id}")

    def test_adjust_bag(self):
        """
        A test to adjsut bag quantity
        """

        response = self.client.post(self.adjust_bag, data={'quantity': '2'})
        response = self.client.post(self.view_bag)
        context = response.context
        self.assertNotEqual(context["bag_items"], [])
        self.assertEqual(context["bag_items"][0]["quantity"], 2)

    def test_delete_item_from_bag(self):
        """
        A test to test deleting products from the shopping bag
        """
        self.client.post(self.adjust_bag,
                         data={'quantity': '1'})
        response = self.client.post(self.remove_from_bag)
        response = self.client.post(self.view_bag)
        context = response.context
        self.assertNotEqual(context["bag_items"], [])
