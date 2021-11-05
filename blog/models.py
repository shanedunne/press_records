from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Blog(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=254)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    content = HTMLField(null=False, blank=False)

    def __str__(self):
        return self.title
