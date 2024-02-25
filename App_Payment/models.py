from django.db import models
from django.conf import settings
# Create your models here.

class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #additional_info = models.TextField(max_length=300, blank=True)
    compnay_name=models.CharField(max_length=150)

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
