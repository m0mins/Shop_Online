from django.db import models
from django.conf import settings
from App_Accounts.models import User
# Create your models here.

class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstName=models.CharField(max_length=100 ,blank=True,null=True)
    lastName=models.CharField(max_length=100 ,blank=True,null=True)
    country = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=30, blank=True)
    postalCode = models.CharField(max_length=10, blank=True)
    company_name=models.CharField(max_length=264, blank=True)
    email=models.CharField(max_length=100 ,blank=True,null=True)
    phone=models.CharField(max_length=100 ,blank=True,null=True)
    address = models.CharField(max_length=264, blank=True)
    additional_info = models.TextField(max_length=264, blank=True)
    

    def __str__(self):
        return f'{self.user.profile.username} billing address'

    def is_fully_filled(self):
        field_names = [f.name for f in self._meta.get_fields()]

        for field_name in field_names:
            value = getattr(self, field_name)
            if value is None or value=='':
                return False
        return True


    class Meta:
        verbose_name_plural = "Billing Addresses"
