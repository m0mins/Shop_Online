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
    user=request.user
    order=Order.objects.filter(user=user,Ordered=False)
    total_orders=0
    if order.exists():
        total_orders +=order[0].orderitems.count()
        order=order[0]
    carts=Cart.objects.filter(user=user,purchased=False)
    cart_items=[]
    total_price=0.0
    for card_item in carts:
        total_price +=float(card_item.get_total())
        cart_items.append(card_item)

    context={
        'order':'order',
        'cart_items':'cart_items',
        'total_orders':'total_orders'
    }
    
    return render( request,'App_Payment/checkout.html',context)