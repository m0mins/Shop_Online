# Authetication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
#from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings
from App_Accounts.models import User,Profile
import uuid
from django.core.mail import send_mail
# Forms and Models
from App_Accounts.models import Profile
#from App_Login.forms import ProfileForm, SignUpForm

# Messages
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        password1=request.POST.get('pass1')
        
        if password is not None:
            if password !=password1:
                messages.error(request,"Password Mismatchd")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"Email already taken")
                    return HttpResponseRedirect(reverse('App_Accounts:register'))
                auth_token=str(uuid.uuid4())
                user=User.objects.create(name=name,email=email,password=password,auth_token=auth_token)
                user.set_password(password)           
                user.save()
                send_email(email,auth_token)
                return HttpResponseRedirect(reverse('App_Accounts:success'))
    return render(request, 'App_Accounts/registration.html')


def send_email(email,auth_token):
    subject='Account verify link'
    message=f'Hi clink the link to create your account http://127.0.0.1:8000/accounts/verify/{auth_token}'
    email_from=settings.EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)

def verify(request,auth_token):
    prof=User.objects.get(auth_token=auth_token)
    prof.is_varified=True
    prof.save()
    messages.success(request, "Account Created Successfully!")
    return HttpResponseRedirect(reverse('App_Accounts:login'))

def success(r):
    return render(r,'App_Accounts/success.html')


