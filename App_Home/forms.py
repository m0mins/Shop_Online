from django import forms
from App_Home.models import ContactUs



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        #fields = ['address', 'zipcode', 'city', 'country']
        fields='__all__'
        #exclude = ['user']

        