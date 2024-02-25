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
    #order=Order.objects.filter(user=request.user,ordered=False)
    #total_orders=0
    #if order.exists():
    #    total_orders +=order[0].orderitems.count()
    #    order=order[0]
    #carts=Cart.objects.filter(user=request.user,purchased=False)
    #cart_items=[]
    #total_price=0.0
    #for card_item in carts:
    #    total_price +=float(card_item.get_total())
    #    cart_items.append(card_item)
#
    #context={
    #    'order':'order',
    #    'cart_items':'cart_items',
    #    'total_orders':'total_orders',
    #    'total_price':'total_price',
    #    'carts':'carts'
#
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders = Order.objects.filter(user=request.user, ordered=False)
    if carts.exists() and orders.exists():
        order = orders[0]
        return render(request, 'App_Payment/checkout.html', context={'carts':carts, 'order':order})
    else:
        messages.warning(request, "You don't have any item in your cart!")
        return redirect("App_Home:home")
    
    
   