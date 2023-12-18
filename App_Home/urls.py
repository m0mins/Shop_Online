from django.urls import path
from App_Home import views


app_name='App_Home'

urlpatterns = [
    path('',views.home ,name='home'),
]