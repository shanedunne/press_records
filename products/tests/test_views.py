from django.test import TestCase
from products.models import Product

class TestProductViews(TestCase):

    def test_get_all_products_page(self):
        """
        A test to test the products page is returned
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_detail_page(self):
        """
        A test to test the products detail is returned
        """

        product = Product.objects.create(
            name='New Product',
            price='20.95',
            description='test description'
        )
        response = self.client.get(f'/product_detail/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')


    def test_get_add_products_page(self):
        """
        A test to get the add product page
        """
        response = self.client.get('/add_product/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')


    def test_get_edit_products_page(self):
        """
        A test to get the edit product page
        """
        product = Product.objects.create(
            name='New Product',
            price='20.95',
            description='test description'
        )
        response = self.client.get(f'/edit_product/{product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')


    def test_delete_product(self):
        """
        A test to test deleting products
        """
        product = Product.objects.create(
            name='New Product',
            price='20.95',
            description='test description'
        )
        response = self.client.get(f'/delete_product/{product.id}')
        self.assertRedirects(response, 'products/products.html')