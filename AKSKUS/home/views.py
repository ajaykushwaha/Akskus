from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import UserPost

def home(request):
    list=UserPost.objects.filter(name__icontains='a')
    return render(request,'index.html',{'some':list})
