from django.forms import ModelForm
from App_Accounts.models import Profile

from django.contrib.auth.forms import UserCreationForm


# forms

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)