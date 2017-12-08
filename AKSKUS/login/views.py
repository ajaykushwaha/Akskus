from django.shortcuts import render
from django.http import HttpResponse


def login(request):

    return render(request,'login/log_and_signup.html')

def idcheck(request,ida):

    return render(request,'login/result.html',{'ida':ida})
