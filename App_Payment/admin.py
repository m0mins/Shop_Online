from django.contrib import admin
from App_Payment.models import BillingAddress
# Register your models here.

class AdminBillingAddress(admin.ModelAdmin):
    list_display=['address','zipcode','city','country']
admin.site.register(BillingAddress,AdminBillingAddress)


