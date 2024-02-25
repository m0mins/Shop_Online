from django.contrib import admin
from App_Payment.models import BillingAddress
# Register your models here.

class AdminBillingAddress(admin.ModelAdmin):
    list_display=['user','additional_info','compnay_name']
admin.site.register(BillingAddress,AdminBillingAddress)


