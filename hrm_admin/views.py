from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def BusinessStrategy(request):
    return render(request=request, template_name="busniess.html")
    
def home(request):
    return render(request=request, template_name="home.html")


def login(request):
    return render(request=request, template_name="login.html")



def NewsFeed(request):
    return render(request=request, template_name="newsfeed.html")


def Onedrive(request):
    return render(request=request, template_name="onedrive.html")


def Organization(request):
    return render(request=request, template_name="organization.html")

    
