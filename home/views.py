from django.shortcuts import render
from products.models import Product

# Create your views here.


def index(request):
    """
    A view to return the index page

    """
    is_feature = Product.objects.filter(is_feature=True)

    context = {
        'is_feature': is_feature,
    }

    return render(request, 'home/index.html', context)
