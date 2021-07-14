from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced

class ProductView(View):
    def get(self,request):
        acoustic = Product.objects.filter(category = 'AG')
        electric = Product.objects.filter(category = 'EG')
        classical = Product.objects.filter(category = 'CG')
        return render(request, 'app/home.html',
        {'acoustic':acoustic, 'electric' : electric, 'classical': classical})


# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',
        {'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
