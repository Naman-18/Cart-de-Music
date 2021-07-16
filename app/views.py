from django.db.models.query import QuerySet
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse

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
 user = request.user
 product_id = request.GET.get('prod_id')
 product = Product.objects.get(id=product_id)
 Cart(user=user,product=product).save()
 return redirect('/cart')
 
def show_cart(request):
    if request.user.is_authenticated:
        user =request.user
        cart = Cart.objects.filter(user=user)
        amount= 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount+=tempamount
            total_amount = amount+shipping_amount
            return render(request,'app/addtocart.html',{'carts':cart,'amount':amount,'shipping': shipping_amount,'totalamount':total_amount})
        else:
            return render(request,'app/emptycart.html')


def plus_cart(request):
    if request.method == 'GET':
        prod_id= request.GET['prod_id']
        c =Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount= 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount+=tempamount
        total_amount = amount+shipping_amount
        data ={'quantity':c.quantity, 'amount':amount,'totalamount':total_amount}
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id= request.GET['prod_id']
        c =Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount= 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount+=tempamount
        total_amount = amount+shipping_amount
        data ={'quantity':c.quantity, 'amount':amount,'totalamount':total_amount}
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id= request.GET['prod_id']
        c =Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount= 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount+=tempamount
        total_amount = amount+shipping_amount
        data ={'amount':amount,'totalamount':total_amount}
        return JsonResponse(data)

def buy_now(request):
 return render(request, 'app/buynow.html')

#def profile(request):
 #return render(request, 'app/profile.html')

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'app/profile.html',{'form':form, 'active':'btn-primary'})
    
    def post(self,request):
        form =CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request, 'Address Added Successfully')
        return render(request,'app/profile.html',{'form':form, 'acitve':'btn=primary'})

def address(request):
 add = Customer.objects.filter(user=request.user)
 return render(request, 'app/address.html', {'add':add, 'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def acousticguitar(request,data=None):
    if data == None:
        guitar = Product.objects.filter(category='AG')
    elif data == 'Fender' or data == 'Cort' or data == 'Yamaha':
        guitar = Product.objects.filter(category='AG').filter(brand=data)
    elif data == 'below':
        guitar = Product.objects.filter(category='AG').filter(discounted_price__lt = 10000)
    elif data == 'above':
        guitar = Product.objects.filter(category='AG').filter(discounted_price__gt = 10000)
    return render(request, 'app/acousticguitar.html',{'guitar':guitar})

def electricguitar(request,data=None):
    if data == None:
        guitar = Product.objects.filter(category='EG')
    elif data == 'Fender' or data == 'Cort' or data == 'Ibanez' or data=='ESP':
        guitar = Product.objects.filter(category='EG').filter(brand=data)
    elif data == 'below':
        guitar = Product.objects.filter(category='EG').filter(discounted_price__lt = 10000)
    elif data == 'above':
        guitar = Product.objects.filter(category='EG').filter(discounted_price__gt = 10000)
    return render(request, 'app/electricguitar.html',{'guitar':guitar})

def classicalguitar(request,data=None):
    if data == None:
        guitar = Product.objects.filter(category='CG')
    elif data == 'Fender' or data == 'Cort' or data == 'Ibanez' or data =='Yamaha' or data=='Epiphone' or data=='Valencia':
        guitar = Product.objects.filter(category='CG').filter(brand=data)
    elif data == 'below':
        guitar = Product.objects.filter(category='CG').filter(discounted_price__lt = 10000)
    elif data == 'above':
        guitar = Product.objects.filter(category='CG').filter(discounted_price__gt = 10000)
    return render(request, 'app/classicalguitar.html',{'guitar':guitar})

#def login(request):
# return render(request, 'app/login.html')

#def customerregistration(request):
 #return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})
    
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Registered Successfully')
            form.save()

        return render(request, 'app/customerregistration.html',{'form':form})



def checkout(request):
 return render(request, 'app/checkout.html')

