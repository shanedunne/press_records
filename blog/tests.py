from django.test import TestCase
from blog.models import Blog
from django.contrib.auth.models import User
from django.urls import reverse


class TestBlogViews(TestCase):

    def setUp(self):
        """
        Set up requirements for view testing
        """

        self.super_user = User.objects.create_superuser(
            username='testsuper',
            email='testadmin@email.com',
            password='testpassword'
        )

        self.blog = Blog.objects.create(
            title='Test Blog',
            author=self.super_user,
            content='test content',
            image='test_image.png'
        )
        self.all_blogs = reverse("all_blogs")
        self.blog_post = reverse("blog_post",
                                 kwargs={"blog_id": self.blog.id})
        self.edit_blog = reverse("edit_blog",
                                 kwargs={"blog_id": self.blog.id})
        self.delete_blog = reverse("delete_blog",
                                   kwargs={"blog_id": self.blog.id})

    def test_get_all_blogs_page(self):
        """
        A test to test the blogs page is returned
        """
        response = self.client.get(self.all_blogs)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/all_blogs.html')

    def test_get_blog_post_page(self):
        """
        A test to test the individual blog post page
        """

        response = self.client.get(self.blog_post)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_post.html')

    def test_get_add_blogs_page(self):
        """
        A test to get the add blog page
        """
        self.client.login(
            username="testsuper", password="testpassword")
        response = self.client.get('/blog/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/add_blog.html')

    def test_get_edit_blog_page(self):
        """
        A test to get the edit blog post
        """

        self.client.login(
            username="testsuper", password="testpassword")
        response = self.client.get(self.edit_blog)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit_blog.html')

    def test_delete_blog(self):
        """
        A test to test deleting blog posts
        """
        self.client.login(
            username="testsuper", password="testpassword")
        response = self.client.get(self.delete_blog)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.all_blogs)
