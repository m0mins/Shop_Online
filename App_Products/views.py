from django.shortcuts import render

# Import views
from django.views.generic import ListView, DetailView

# Models
from App_Products.models import Product

# Mixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



class Home(ListView):
    model = Product
    template_name = 'App_Home/home.html'

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Products/product_detail.html'