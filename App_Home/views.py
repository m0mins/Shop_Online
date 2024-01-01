from django.shortcuts import render
from App_Home.models import Slider
from App_Products.models import Product,Category,Sub_Category

# Create your views here.
def home(request):
    slider=Slider.objects.all()
    categories=Category.objects.all()
    categories_with_subcategories = {}
    for category in categories:
        subcategories = Sub_Category.objects.filter(categorys=category)
        categories_with_subcategories[category] = subcategories

    return render(request,'App_Home/home.html',context={'slider':slider,'categories_with_subcategories': categories_with_subcategories})
