from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
#from .models import
import json


# Create your views here.

def index(request):
    return render(request,'education/home.html')

def login(request):
    return render(request,'education/login.html')

def signup(request):
    return render(request,'education/signup.html')