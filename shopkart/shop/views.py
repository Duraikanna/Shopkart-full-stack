from http.client import HTTPResponse
from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.http import HttpResponse
from shop.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout




# Create your views here.
def home(request):
    products=product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"products":products})


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logged out successfully")
    return redirect("/")

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"logged in successfully")
                return redirect("/")
            else:
                messages.error(request,"invalid User Name or Password")
                return redirect("/login")
    return render(request,"shop/login.html")
def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration success You can Login Now ..!")
            return redirect('/login')
    return render(request,"shop/register.html",{'form':form})

def collections(request):
    Catagory=catagory.objects.filter(status=0)
    return render(request,"shop/collections.html",{"Catagory":Catagory})



def collectionsview(request,name):
    if(catagory.objects.filter(name=name,status=0)):
        print("Condition being true")
        products=product.objects.filter(catagory__name=name)
        return render(request,"shop/products/index.html",{"products":products,"category_name":name})
    else:
        print("Condition being False")

        messages.warning(request,"no such Catagory found")
        return redirect('collections')


def product_details(request,cname,pname):
    if(catagory.objects.filter(name=cname,status=0)):
      if(product.objects.filter(name=pname,status=0)):
        products=product.objects.filter(name=pname,status=0).first()
        return render(request,"shop/products/product_details.html",{"products":products})
      else:
        messages.error(request,"No Such Produtct Found")
        return redirect('collections')
    else:
      messages.error(request,"No Such Catagory Found")
      return redirect('collections')
    


    