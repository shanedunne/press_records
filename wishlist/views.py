from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Wishlist

# Create your views here.

def wishlist(request):
    """
    A view to return a users wishlist
    """
    wishlist = get_object_or_404(Wishlist, user=request.user)

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """ Add product to wishlist """

    wishlist = get_object_or_404(Wishlist, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    if product not in wishlist.products.all():
        wishlist.products.add(product)
        messages.success(request, f"{product.name} has been added to your wishlist")
    else:
        messages.error(request, 'Error adding product to wishlist')
    return redirect(reverse("product_detail", args=[product_id]))


@login_required
def delete_wishlist_item(request, product_id):
    """ Delete an item from the wishlist """
    
    wishlist = get_object_or_404(Wishlist, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(request, f"{product.name} has been removed from your wishlist")
    else:
        messages.error(request, "Error, please try again")
    return redirect(reverse('wishlist'))
