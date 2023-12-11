from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello-world')
def login_page(request):
    return render(request, 'login.html')
'''
members/
├── templates/
│       └── login.html
'''
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect()
            pass
        else:
            return redirect()