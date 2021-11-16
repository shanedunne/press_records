from django.test import TestCase
from .forms import ProductForm
from products.models import Category, Genre, Artist

class TestProductForm(TestCase):

    def test_product_form(self):

        category = Category.objects.create(
            name="test_category",
            freindly_name="Test Category",

        artist = Artist.objects.create(
            name="test_artist",

        genre = Genre.objects.create(
            name="test_genre",

        form = ProductForm({
            'category': category,
            'sku': '1',
            'name': 'test name',
            'artist_name': artist,
            'description': 'test description',
            'genre': genre,
            'price': '2.99',
            'is_feature': False,
            'is_hifi_deal': False,
            'rating': 5,
            'image_url': 'test.url',
        })
        self.assertTrue(form.is_valid())
