from django.shortcuts import render, get_object_or_404, redirect

# Authentications
from django.contrib.auth.decorators import login_required

# Model
from App_Order.models import Cart, Order
from App_Products.models import Product
# Messages
from django.contrib import messages
# Create your views here.

@login_required  
def checkout(request):
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders = Order.objects.filter(user=request.user, ordered=False)
    if request.method=='POST':
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        country=request.POST.get('country')
        city=request.POST.get('city')
        postalCode=request.POST.get('postalCode')
        company=request.POST.get('company')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        additional_info=request.POST.get('additional_info')
    if carts.exists() and orders.exists():
        order = orders[0]
    

        #return render(request, 'App_Payment/checkout.html', context={'carts':carts, 'order':order})
    #else:
        #messages.warning(request, "You don't have any item in your cart!")
        #return redirect("App_Home:home")
    
    
   