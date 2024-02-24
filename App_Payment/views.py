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
    return render( request,'App_Payment/checkout.html')