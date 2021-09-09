from django.shortcuts import render
from .models import Blog

# Create your views here.

def base(request):
    blogs = Blog.objects
    return render(request, 'base.html',{'blogs':blogs})

def new(request):
    return render(request, 'new.html')