import email
from unicodedata import name
from unittest import result
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.test import RequestFactory
from myapp.models import Contact




# Create your views here.
def deshboard(request):
    return render(request, 'home.html')
def home(request):
    return render(request, 'home.html')
def register(request): 
    return render(request, 'register.html')
def about(request):
    return render(request, 'about.html')










def contact(request):
    if request.method == "POST":
        name =request.POST['name']
        email =request.POST['email']
        desc =request.POST['desc']
        values =Contact(name = name , email = email, desc =desc)
        values.save()
    return render(request, 'register.html')












def add(request):
    if request.method == "POST":
        print("HElo")

    return render(request, 'about.html',{})
    