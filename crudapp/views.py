from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Blog

# Create your views here.

def base(request):
    blogs = Blog.objects
    return render(request, 'base.html',{'blogs':blogs})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.now()
    blog.save()
    return redirect ('base')