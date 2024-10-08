from django.shortcuts import render
from App_Home.models import Slider
from App_Products.models import Product,Category,Sub_Category
from App_Home.models import ContactUs
from App_Home.forms import ContactUsForm
from django.core.mail import send_mail

import requests

from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
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


def contact(request):
    return render(request,'App_Home/contact.html')

from django.shortcuts import render

# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)



def contactUs(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        services=request.POST.get('services')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')

        note=request.POST.get('note')
        contact=ContactUs.objects.create(name=name,email=email,address=address,services=services,subject=subject,phone=phone,message=note)

        contact.save()
        print("finally saved ######################################")
        email_subject = f'New contact {email}: {subject}'
        #email_message = note
        email_message = f'Name : {name}\n Phone Number : {phone}\n Message : {note}'

        #recipient_list = settings.EMAIL_HOST_USER
        #from_email = email

        #recipient_list = settings.EMAIL_HOST
        print("print  from inside form method #############******************#######################")
        send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)

        #send_mail(email_subject, email_message, from_email, recipient_list)
        return redirect("App_Home:home")
            #return render(request, 'contact/success.html')
    #form = ContactUsForm()
    #context = {'form': form}
    #return render(request, 'contact/contact.html', context)
    return render(request, 'App_Home/contact.html')