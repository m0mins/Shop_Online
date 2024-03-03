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
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
#from App_Login.forms import ProfileForm, SignUpForm

# Messages
from django.contrib import messages

import random

def generate_otp(length=6):
    return ''.join(random.choice('0123456789') for _ in range(length))

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
                otp = generate_otp()
                
                #auth_token=str(uuid.uuid4())
                #user=User.objects.create(username=username,email=email,password=password,auth_token=auth_token)
                user=User.objects.create(username=username,email=email,password=password)
                user.set_password(password)           
                user.save()
                send_email(email, otp)
                request.session['otp'] = otp
                request.session['email'] = email
                #send_email(email,auth_token)
                return HttpResponseRedirect(reverse('App_Accounts:verify_account'))
                #return redirect('verify_account')
    return render(request, 'App_Accounts/registration.html')


#def send_email(email, auth_token):
def send_email(email, auth_token):
    #base_url = settings.BASE_URL  # Assuming BASE_URL is defined in your settings

    # Use reverse to dynamically generate the URL based on your URL patterns
    #verify_url = reverse('App_Accounts:verify_account', kwargs={'auth_token': auth_token})

    # Combine the base URL and the dynamically generated URL
    #full_url = f'{base_url}{verify_url}'

    #subject = 'Account verify link'
    #message = f'Hi, click the link to create your account: {full_url}'
    #email_from = settings.EMAIL_HOST_USER
    #recipient = [email]
    #send_mail(subject, message, email_from, recipient)
    subject = 'Your OTP for authentication'
    message = f'Your OTP is: {auth_token}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)

#def verify_account(request,auth_token):
#    prof=User.objects.get(auth_token=auth_token)
#    prof.is_varified=True
#    prof.save()
#    messages.success(request, "Account Created Successfully!")
#    return HttpResponseRedirect(reverse('App_Accounts:login'))
def verify_account(request):
    if request.method == 'POST':
        user=request.user
        prof=User.objects.get(user=user)
        user_entered_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        email = request.session.get('email')
        tr=User.objects.filter(email=email)

        if user_entered_otp == stored_otp and email==tr:
            prof.is_varified=True
            prof.save()
            messages.success(request, "Account Created Successfully!")
            return HttpResponseRedirect(reverse('App_Accounts:login'))
            # OTP is correct, perform authentication logic here
            # For example, you can log the user in

            #return redirect('home')

    return render(request, 'App_Accounts/verify.html')

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
    return render(request, 'App_Accounts/profile.html', context)


def forgot_pass(request):
    if request.method == 'POST':
        email=request.POST.get("email")
        user=User.objects.get(email=email)
        db_auth=user.auth_token
        reset_send_email(email,db_auth)
        return HttpResponseRedirect(reverse('App_Accounts:success'))
    return render(request,'App_Accounts/forgot.html')

def reset_send_email(email,auth_token):
    base_url = settings.BASE_URL  # Assuming BASE_URL is defined in your settings

    # Use reverse to dynamically generate the URL based on your URL patterns
    verify_url = reverse('App_Accounts:reset_verify', kwargs={'auth_token': auth_token})

    # Combine the base URL and the dynamically generated URL
    full_url = f'{base_url}{verify_url}'

    subject = 'Reset password link'
    message = f'Hi, click the link to reset your password: {full_url}'
    email_from = settings.EMAIL_HOST_USER
    recipient = [email]
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
    user = request.user
    profile_instance = Profile.objects.get(user=user)

    if request.method == 'POST':
        # Update the profile instance with the new data from the form
        profile_instance.first_name = request.POST.get('first_name')
        profile_instance.last_name = request.POST.get('last_name')
        profile_instance.address_1 = request.POST.get('address_1')
        profile_instance.country = request.POST.get('country')
        profile_instance.city = request.POST.get('city')
        profile_instance.zipcode = request.POST.get('zipcode')

        if 'image' in request.FILES:       
            profile_instance.image = request.FILES['image']
        # Add other fields as needed
        profile_instance.save()
        return redirect(request.META['HTTP_REFERER'])

        #return redirect("App_Home:home") # Redirect to a view showing the updated profile

    return render(request, 'App_Accounts/profile_update.html', {'profile_instance': profile_instance})
    
