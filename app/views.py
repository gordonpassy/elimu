from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required(login_url='/accounts/login/')
def index(request):
    test = "Working!!"
    return render (request,'index.html',{"test":test})
