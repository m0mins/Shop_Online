from django.shortcuts import render, HttpResponseRedirect, redirect,get_object_or_404
# Import views
from django.views.generic import ListView, DetailView

# Models
from App_Products.models import Product,Product_Size,Category,Sub_Category

# Mixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Products/product_detail.html'

def category(request):
    # Retrieving all instances of the Product model
    all_products = Product.objects.all()

    # Creating a list to store product details (name and sizes)
    product_details = []

    # Iterating through the products
    for product in all_products:
        # Retrieving related size variants using the reverse relation
        size_variants = product.size_variants.all()
        color_variants = product.color_variants.all()

        # Creating a dictionary to store product details
        product_detail = {
            'name': product.name,
            'sku':product.sku,
            'price':product.price,
            'old_price':product.old_price,
            'mainimage':product.mainimage,

            'category':product.category.title,
            'sub_category':product.sub_category.title,

            'sizes': [size_variant.size.name for size_variant in size_variants],
            'colors':[color_variant.color.name for color_variant in color_variants]
        }

        # Adding the product detail dictionary to the list
        product_details.append(product_detail)

    # Passing the list of product details to the template
    context = {'product_details': product_details}

    # Rendering the template
    return render(request, 'App_Products/Category/men_cloth.html', context)

def sub_men_cloth(request,category):
    try:
        # Retrieve the category object
        category = Category.objects.get(title=category)
        # Query all products in the specified category
        products_in_category = Product.objects.filter(category=category)
        # Pass the category and products to the template
        context = {'category': category, 'products': products_in_category}
        return render(request, 'App_Products/Category/sub.html', context)

    except Category.DoesNotExist:
        # Handle the case where the specified category does not exist
        return render(request, 'App_Products/Category/category_not_found.html')


class SubCategoryProductListView(ListView):
    model = Product
    template_name = 'App_Products/Sub_Category/sub_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        sub_category = get_object_or_404(Sub_Category, id=self.kwargs['sub_category_id'])
        return Product.objects.filter(sub_category=sub_category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_category'] = get_object_or_404(Sub_Category, id=self.kwargs['sub_category_id'])
        return context