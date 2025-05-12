from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User, auth

def home(request): 
    return render(request, 'uniapp/home.html')
