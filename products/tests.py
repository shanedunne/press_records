from django.test import TestCase
from products.models import Product
from django.contrib.auth.models import User
from django.urls import reverse


class TestProductViews(TestCase):

    def setUp(self):
        """
        Set up requirements for view testing
        """

        self.super_user = User.objects.create_superuser(
            username='testsuper',
            email='testadmin@email.com',
            password='testpassword'
        )

        self.product = Product.objects.create(
            name='New Product',
            price='20.95',
            description='test description'
        )
        self.products = reverse("products")
        self.product_detail = reverse("product_detail",
                                      kwargs={"product_id": self.product.id})
        self.edit_product = reverse("edit_product",
                                    kwargs={"product_id": self.product.id})
        self.delete_product = reverse("delete_product",
                                      kwargs={"product_id": self.product.id})

    def test_get_all_products_page(self):
        """
        A test to test the products page is returned
        """
        response = self.client.get(self.products)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_detail_page(self):
        """
        A test to test the products detail is returned
        """

        response = self.client.get(self.product_detail)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_get_add_products_page(self):
        """
        A test to get the add product page
        """
        self.client.login(
            username="testsuper", password="testpassword")
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_get_edit_products_page(self):
        """
        A test to get the edit product page
        """

        self.client.login(
            username="testsuper", password="testpassword")
        response = self.client.get(self.edit_product)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')

    def test_delete_product(self):
        """
        A test to test deleting products
        """
        self.client.login(
            username="testsuper", password="testpassword")
        response = self.client.get(self.delete_product)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.products)
