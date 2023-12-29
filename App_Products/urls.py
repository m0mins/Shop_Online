from django.urls import path
from App_Products import views
from .views import SubCategoryProductListView

app_name='App_Products'

urlpatterns = [
    path('cate/',views.category,name='cate'),
    path('sub/<str:category>/',views.sub_men_cloth,name='sub'),
    path('sub_category/<int:sub_category_id>/', SubCategoryProductListView.as_view(), name='sub_category_products'),

]