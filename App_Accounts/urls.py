from django.urls import path
from App_Accounts import views


app_name='App_Accounts'

urlpatterns = [
  
    path('register/',views.register, name='register'),
    path('success/',views.success, name='success'),
    path('verify/<auth_token>/',views.verify, name='verify'),
  
    
]