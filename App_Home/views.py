from django.shortcuts import render
from App_Home.models import Slider
# Create your views here.
def home(request):
    slider=Slider.objects.all()
    return render(request,'App_Home/home.html',context={'slider':slider})