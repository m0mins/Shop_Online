from django.urls import path
from App_Accounts import views


app_name='App_Accounts'

urlpatterns = [
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register, name='register'),
    path('success/',views.success, name='success'),
    path('verify/<auth_token>/',views.verify, name='verify'),
    path('customer_details/<int:pk>/',views.customerDetails,name='customer_details'),
    
]