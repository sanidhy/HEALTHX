from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse


# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("this is about")

def temp_nav(request):
    return render(request,'temp_nav.html')

def teamsignup(request):
    return render(request,'teampageup.html')


def button(request):
    return render(request,'button.html')

def services(request):
    return HttpResponse("this is services")

def new(request):
    return render(request,'new.html')

def signup(request):
    return render(request,'signup.html')