from django.contrib import admin
from App_Payment.models import BillingAddress,BillingAddr
# Register your models here.

admin.site.register(BillingAddress)
admin.site.register(BillingAddr)
#class AdminBillingAddress(admin.ModelAdmin):
#    list_display=['user','company_name','additional_info']
#admin.site.register(BillingAddress,AdminBillingAddress)


