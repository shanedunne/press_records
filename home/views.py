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


def page_not_found(request, *args, **argv):
    return render(request, 'home/404.html')


def bad_request(request, *args, **argv):
    return render(request, 'home/400.html')


def permission_denied(request, *args, **argv):
    return render(request, 'home/403.html')


def server_error(request, *args, **argv):
    return render(request, 'home/500.html')

