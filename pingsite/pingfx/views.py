from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Websites, Users

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def createUser(request, user, email)

def createWebsite(request, user, URL)

def getEmail(request, user)

def getURLs(request, user)

def editURL(request, user, URL, new_URL)

def editEmail(request, user, new_email)

def deleteUser(request, user)

def deleteURL(request, user, URL)
