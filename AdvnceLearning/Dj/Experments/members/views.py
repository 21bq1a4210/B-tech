from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . forms import RegisterUserForm

'''
members/
├── templates/
│       └── login.html
'''

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello-world')
def login_page(request):
    return render(request, 'login.html')

def home(req):
    return render(req, 'home.html')
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your homepage URL
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return render(request, 'login.html')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You were logged out')
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration success!')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register.html', {'form': form})
