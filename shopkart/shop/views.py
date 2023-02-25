from django.shortcuts import render
from products.models import Product


# Create your views here.
def home(request):
    products = Product.objects.filter(trending=1)
    return render(request, "shop/index.html", {"products": products})
