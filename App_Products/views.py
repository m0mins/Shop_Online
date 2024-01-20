from django.shortcuts import render, HttpResponseRedirect, redirect,get_object_or_404,Http404
from django.views.generic import ListView, DetailView

from App_Products.models import Product,Product_Size,Category,Sub_Category
from App_Order.models import Cart

from django.contrib.auth.mixins import LoginRequiredMixin



def all_products(request):

        products = Product.objects.all()
        product_details = []

        for product in products:
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

        context = {'combined_data': combined_data}

        return render(request, 'App_Products/Category/all_products.html', context)



def category_products(request, category_name, subcategory_name=None):
    category = get_object_or_404(Category, title=category_name)

    selected_subcategory = None
    subcategory_products = []

    if subcategory_name:
        selected_subcategory = get_object_or_404(Sub_Category, title=subcategory_name, categorys=category)
        subcategory_products = selected_subcategory.sub_category.all()

    products = Product.objects.filter(category=category)
    subcategories = Sub_Category.objects.filter(categorys=category)

    context = {
         
        'category': category,
        'products': subcategory_products if subcategory_name else products,
        'subcategories': subcategories if not subcategory_name else [],
        'selected_subcategory': selected_subcategory,
        'subcategory_products': subcategory_products,
        'subcategory':subcategory_name
    }

    return render(request, 'App_Products/Sub_Category/category_products.html', context)

def single_product(request, pk):
    
    product = Product.objects.get(id=pk)
    
    size_variants = product.size_variants.all()
    color_variants = product.color_variants.all()

    context = {
        'product_id':product.id,
        'name': product.name,
        'price': product.price,
        'old_price': product.old_price,
        'preview': product.preview_text,
        'description': product.detail_text,
        'additional_info': product.additional_info,
        'sizes': [size_variant.size.name for size_variant in size_variants],
        'colors': [color_variant.color.name for color_variant in color_variants],
        'sku': product.sku,
        'category': product.category.title,
        'mainimage': product.mainimage,
   
    }

    return render(request, 'App_Products/single_product.html', context)

def shop_products(request):
        
    products = Product.objects.all()
    new_added=products.order_by('-id')[:3]
    product_details = []

    for product in products:
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

    context = {'combined_data': combined_data,'new_added':new_added}

    return render(request, 'App_Products/shop_products.html', context)
