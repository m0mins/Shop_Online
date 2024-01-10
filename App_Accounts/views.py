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
from django.contrib.auth import update_session_auth_hash
# Forms and Models
from App_Accounts.forms import ProfileForm
from App_Accounts.models import Profile
#from App_Login.forms import ProfileForm, SignUpForm

# Messages
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
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
                user=User.objects.create(username=username,email=email,password=password,auth_token=auth_token)
                user.set_password(password)           
                user.save()
                send_email(email,auth_token)
                return HttpResponseRedirect(reverse('App_Accounts:success'))
    return render(request, 'App_Accounts/registration.html')


def send_emailss(email,auth_token):
    subject='Account verify link'
    base_url = settings.BASE_URL
    message=f'Hi clink the link to create your account http://127.0.0.1:8000/accounts/verify/{auth_token}'
    email_from=settings.EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)


def send_email(email, auth_token):
    base_url = settings.BASE_URL  # Assuming BASE_URL is defined in your settings

    # Use reverse to dynamically generate the URL based on your URL patterns
    verify_url = reverse('verify_account', kwargs={'auth_token': auth_token, 'email': email})

    # Combine the base URL and the dynamically generated URL
    full_url = f'{base_url}{verify_url}'

    subject = 'Account verify link'
    message = f'Hi, click the link to create your account: {full_url}'
    email_from = settings.EMAIL_HOST_USER
    recipient = [email]
    send_mail(subject, message, email_from, recipient)

def verify(request,auth_token):
    prof=User.objects.get(auth_token=auth_token)
    prof.is_varified=True
    prof.save()
    messages.success(request, "Account Created Successfully!")
    return HttpResponseRedirect(reverse('App_Accounts:login'))

def success(r):
    return render(r,'App_Accounts/success.html')

def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('App_Home:home'))
    else:

        if request.method == 'POST':
            email=request.POST.get("email")
            password=request.POST.get("password")
            user = authenticate(email=email, password=password)
    
            if user is not None:
                login(request, user)              
                return HttpResponseRedirect(reverse('App_Home:home'))
            else:
                return HttpResponse('Invalid login credentials')
        return render(request, 'App_Accounts/login.html')

@login_required
def logout_user(request):
    logout(request)
    messages.warning(request, "You are logged out!!")
    return redirect("App_Home:home")

@login_required
def customerDetails(request, pk):
    customerId = User.objects.get(id=pk)
    context = {'customerId':customerId}
    return render(request, 'App_Accounts/profile2.html', context)


def forgot_pass(request):
    if request.method == 'POST':
        email=request.POST.get("email")
        user=User.objects.get(email=email)
        db_auth=user.auth_token
        reset_send_email(email,db_auth)
        return HttpResponseRedirect(reverse('App_Accounts:success'))
    return render(request,'App_Accounts/forgot.html')

def reset_send_email(email,auth_token):
    subject='Reset Password link'
    message=f'Hi clink the link to Reset Your Password http://127.0.0.1:8000/accounts/reset_verify/{auth_token}'
    email_from=settings.EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)

def reset_verify(request,auth_token):
    user=User.objects.get(auth_token=auth_token)
    if user:
        
        if request.method=='POST':
            
            password=request.POST.get('pass')
        
            password1=request.POST.get('pass1')
            if password==password1:
                
                user.set_password(password)
                user.save()
                update_session_auth_hash(request,user)
                messages.success(request, "Password Changed Successfully!")
                return redirect("App_Accounts:login")
            else:
                return redirect(request.META['HTTP_REFERER'])
            
       
        return render(request,'App_Accounts/reset_pass.html')
    else:
        
        messages.success(request, "Wrong Email Address!")
        return render(request,'App_Accounts/forgot.html')

@login_required
def profile_update(request):
    current_user = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=current_user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, "Profile Updated Successfully!!")
            return redirect("App_Home:home")
    return render(request, 'App_Accounts/profile_update.html', context={'form':form})

def profile2(request):
    return render(request,'App_Accounts/profile2.html')
    
