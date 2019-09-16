from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Website, User

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def createUser(request, user, email):
    newUser = User(user=user, email=email)
    newUser.save()
    return HttpResponse("I just created a new user {} with email {}.".format(user, email))

# def createWebsite(request, user, URL)

def getEmail(request, user):
    getUser = User.objects.get(user=user)
    return HttpResponse("The email address for {} is {}.".format(user, getUser.email))

# def getURLs(request, user)

# def editURL(request, user, URL, new_URL)

def editEmail(request, user, new_email):
    editUser = User.objects.get(user=user)
    editUser.email = new_email
    editUser.save()
    return HttpResponse("The email address for {} is now {}.".format(user, editUser.email))    

def deleteUser(request, user):
    deleteUser = User.objects.get(user=user)
    deleteUser.delete()
    return HttpResponse("Deleted user {}.".format(user))

# def deleteURL(request, user, URL)
