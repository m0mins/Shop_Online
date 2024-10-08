from django.db import models
from django.conf import settings

from django.core.validators import EmailValidator
# Create your models here.

class Slider(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='slider_images/')

    def __str__(self):
        return self.title
    

class ContactUs(models.Model):
    SERVICES_CHOICE = [
        ('Architecture', 'Architecture'),
        ('The Rehearsal Dinner', 'The Rehearsal Dinner'),
        ('The Afterparty', 'The Afterparty'),
        ('Videographers', 'Videographers'),
        ('Perfect Cake', 'Perfect Cake'),
        ('All Of The Above', 'All Of The Above')
    ]
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=False, blank=False)
    address = models.CharField(max_length=255)
    #services = models.CharField(max_length=15)
    services = models.CharField(max_length=80, choices=SERVICES_CHOICE, default='Architecture')
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=264, blank=True)

    def __str__(self):
        return self.subject