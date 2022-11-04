from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.


def index(request):
    return HttpResponse("Hello world");
    
def hello_html(request):
    return HttpResponse("""
    <h1>Happy Coding</h1>""")

def hello(request,name):
    return HttpResponse(f"Hello {name.capitalize()}");

