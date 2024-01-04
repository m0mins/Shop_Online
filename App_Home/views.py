from django.shortcuts import render
from App_Home.models import Slider
from App_Products.models import Product,Category,Sub_Category
import requests
# Create your views here.
def home(request):
    slider=Slider.objects.all()
    product_url = 'http://127.0.0.1:8000/products/all_products'
    product_response = requests.get(product_url)
    product_content = product_response.text 
    categories=Category.objects.all()
    categories_with_subcategories = {}
    for category in categories:
        subcategories = Sub_Category.objects.filter(categorys=category)
        categories_with_subcategories[category] = subcategories

    return render(request,'App_Home/home.html',context={'slider':slider,'product_content':product_content,'categories_with_subcategories': categories_with_subcategories})
