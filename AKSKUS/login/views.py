from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout


def login_in(request):
    if request.method == "POST":
        '''
        username = request.POST.get('id', 'no_such_thing')
        password = request.POST.get('pass', 'no_such_thing')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'login/Loggedin.html', {'username': username})
        else:
            return render(request, 'login/Loggedin.html', {'username': 'Invalid login'})
        '''
        return render(request, 'login/Loggedin.html', {'username': username})
    else:
        return render(request, 'login/Loggedin.html',{ 'username': 'Invalid login' })