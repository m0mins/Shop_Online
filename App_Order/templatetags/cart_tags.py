from django import template
from App_Order.models import Order,Product

register=template.Library()

@register.filter
def cart_total(user):
    order=Order.objects.filter(user=user, ordered=False)

    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0

@register.filter
def get_product_count(category):
    products=Product.objects.filter(category=category)
    if products.exists():
        return products.count()
    else:
        return 0
