from django.shortcuts import render

# Create your views here.

def wishlist(request):
    """
    A view to return a users wishlist
    """
    return render(request, 'wishlist/wishlist.html')