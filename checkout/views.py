from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Jb4FjAhGJpAzUlLXI9K9klGCO3hJIxouBsC88OIw9Mdmezxl1NIRQBjIQXliKKTFXoDVIeBM2ovWz773o4l5T0j00svW6xo6k',
        'client_secret': 'test secret'
    }

    return render(request, template, context)