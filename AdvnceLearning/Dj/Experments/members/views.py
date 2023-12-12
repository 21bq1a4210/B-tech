from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello-world')
def login_page(request):
    return render(request, 'login.html')

def home(req):
    return render(req, 'home.html')
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
        #print(username, password)
        if user is not None:
            login(request, user)
            print('login success')
            # Redirect to a success page or homepage after login
            return redirect('home')  # Replace 'home' with the name of your homepage URL
        else:
            # Add an error message if login fails
            print('login failed')
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})

    # If the request method is not POST, render the login form
    return render(request, 'login.html')