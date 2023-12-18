from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import static ,staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('App_Home.urls')),
    path('accounts/',include('App_Accounts.urls')),
    path('cart/',include('App_Cart.urls')),
    path('payment/',include('App_Payment.urls')),
    path('products/',include('App_Products.urls')),
]
urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
