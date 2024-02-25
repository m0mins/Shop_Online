from django.contrib import admin
from App_Payment.models import BillingAddress
# Register your models here.

admin.site.register(BillingAddress)
#class AdminBillingAddress(admin.ModelAdmin):
#    list_display=['user','company_name','additional_info']
#admin.site.register(BillingAddress,AdminBillingAddress)


