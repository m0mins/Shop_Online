from django.urls import path
from App_Products import views

app_name='App_Products'

urlpatterns = [
    #path('all_products/',views.all_products,name='all_products'),

    path('category/<str:category_name>/', views.category_products, name='category_products'),
    path('category/<str:category_name>/<str:subcategory_name>/', views.category_products, name='subcategory_products'),
    path('single_product/<int:pk>/',views.single_product,name='single_product'),
    path('shop_products/',views.shop_products,name='shop_products'),
    path('search_by_category/',views.search_by_category,name='search_by_category'),
    path('search_by_price/',views.search_by_price,name='search_by_price'),

]