from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('App_Home.urls')),
    path('accounts/',include('App_Accounts.urls')),
    path('cart/',include('App_Cart.urls')),
    path('order/',include('App_Order.urls')),
    path('payment/',include('App_Payment.urls')),
    path('products/',include('App_Products.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
