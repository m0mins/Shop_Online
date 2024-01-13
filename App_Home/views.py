from django.shortcuts import render
from App_Home.models import Slider
from App_Products.models import Product,Category,Sub_Category
import requests
# Create your views here.
def home(request):
    #slider=Slider.objects.all()
    #categories=Category.objects.all()
    #categories_with_subcategories = {}

    products = Product.objects.all()
    product_details = []

    for product in products:
        #for product, category in zip(products, categories):
        size_variants = product.size_variants.all()
        color_variants = product.color_variants.all()
        product_detail = {
            'products':products,
            'name': product.name,
            'sku':product.sku,
            'price':product.price,
            'old_price':product.old_price,
            'mainimage':product.mainimage,
            'category':product.category.title,
            'sizes': [size_variant.size.name for size_variant in size_variants],
            'colors':[color_variant.color.name for color_variant in color_variants]
        }

        product_details.append(product_detail)
    combined_data = [{'object': obj, 'product_name': name} for obj, name in zip(products, product_details)]

    #for category in categories:
        #subcategories = Sub_Category.objects.filter(categorys=category)
        #categories_with_subcategories[category] = subcategories
    #return {
        #'slider':slider,
        #'categories_with_subcategories':categories_with_subcategories,
        #'combined_data':combined_data,
    #}

    return render(request,'App_Home/home.html',context={'combined_data':combined_data})