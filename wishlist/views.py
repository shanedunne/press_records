from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product
from .models import Wishlist

# Create your views here.

def wishlist(request):
    """
    A view to return a users wishlist
    """
    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """

    wishlist = get_object_or_404(Wishlist, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    if product not in wishlist.products.all():
        wishlist.products.add(product)
        messages.success(request, f"{product.name} has been added to your wishlist")
        return HttpResponse(status=200)
    else:
        messages.error(request, 'Error adding product to wishlist')
    return redirect(reverse("products", args=[product_id]))
