from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_wishlist(sender, instance, created, **kwargs):
    """
    Create or update the users wishlist
    """
    if created:
        Wishlist.objects.create(user=instance)
    instance.userprofile.save()