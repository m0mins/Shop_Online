from App_Home.models import Slider
from App_Products.models import Product,Category,Sub_Category,Size,Color

def context_processor_data(request):
    slider=Slider.objects.all()
    categories=Category.objects.all()
    all_sizes=Size.objects.all()
    all_colors=Color.objects.all()
    categories_with_subcategories = {}
    for category in categories:
        subcategories = Sub_Category.objects.filter(categorys=category)
        categories_with_subcategories[category] = subcategories
    return{
        'slider':slider,
        'categories':categories,
        'all_sizes':all_sizes,
        'all_colors':all_colors,
        'categories_with_subcategories':categories_with_subcategories
    }