from django.shortcuts import render
from products.models import Product

# Create your views here.


def index(request):
    """
    A view to return the index page

    """
    is_feature = Product.objects.filter(is_feature=True)
    is_hifi_deal = Product.objects.filter(is_hifi_deal=True)

    context = {
        'is_feature': is_feature,
        'is_hifi_deal': is_hifi_deal,
    }

    return render(request, 'home/index.html', context)
