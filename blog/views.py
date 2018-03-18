from django.shortcuts import render
from django.http import HttpResponse
from .models import myBlog
# Create your views here.

myPosts = myBlog.object.all()

myDict = {"htmlVar": myPosts}

def index(request):
    return render(request, "index.html")

def test(request):
    return HttpResponse("<h1>Hello From Test</h1>")
