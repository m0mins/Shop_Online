from django import template
from App_Order.models import Order,Cart
from App_Products.models import Product,Size,Product_Size,Product_Color
from django.db.models import Count

register=template.Library()

@register.filter
def cart_total(user):
    order=Order.objects.filter(user=user, ordered=False)

    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0

@register.filter
def sub_total(user):
    carts = Cart.objects.filter(user=user, purchased=False)
    cart_items = []
    total_price = 0.0

    for cart_item in carts:
        total_price += float(cart_item.get_total())
        cart_items.append(cart_item)

    return {'cart_items': cart_items, 'total_price': total_price}
    #total_price = 0.0
    #total_quantity=0
    #carts = Cart.objects.filter(user=user,purchased=False)

    #for cart_item in carts:
        #total_price += float(cart_item.get_total())
        #total_quantity += cart_item.quantity

    #return {'total_price': total_price, 'total_quantity': total_quantity,'carts':carts}

@register.filter
def get_product_count(category):
    products=Product.objects.filter(category=category)
    if products.exists():
        return products.count()
    else:
        return 0

@register.filter
def product_count_by_size(size):
    size_counts=Product_Size.objects.filter(size=size).count()
    if size_counts:
        return size_counts
    else:
        return 0

@register.filter
def product_count_by_color(color):
    color_counts=Product_Color.objects.filter(color=color).count()
    if color_counts:
        return color_counts
    else:
        return 0
    
