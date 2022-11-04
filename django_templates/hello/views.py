from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World!");


def greet(request,name):
    return render(request,"hello.html",{'user_name':name})
