from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from products.category_models import LaptopCategory, MobileCategory


# Create your views here.

def collections(request):
    category = Category.objects.filter(status=0)
    return render(request, "products/collections.html", {"category": category})


def collectionsview(request, name):
    if Category.objects.filter(name=name, status=0):
        products = Product.objects.filter(category__name=name)
        return render(request, "products/index.html", {"products": products, "category_name": name})
    else:
        messages.warning(request, "no such Catagory found")
        return redirect('collections')


def product_details(request, cname, pname):
    product_info = get_product_info(cname)

    product      = Product.objects.get(name = pname)
    p_info       = product_info.objects.get(product = product)

    print(p_info)
    if Category.objects.filter(name=cname, status=0):
        if Product.objects.filter(name=pname, status=0):
            products = Product.objects.filter(name=pname, status=0).first()
            return render(request, "products/product_details.html",
                          {"products": products,
                           "category": cname.lower(),
                           "product_info" : p_info
                           })
        else:
            messages.error(request, "No Such Produtct Found")
            return redirect('collections')
    else:
        messages.error(request, "No Such Catagory Found")
        return redirect('collections')


def get_product_info(category_name):
    category = None
    category_name = category_name.lower()
    if category_name == "mobile":
        category = MobileCategory
    elif category_name == "laptop":
        category = LaptopCategory

    return category
