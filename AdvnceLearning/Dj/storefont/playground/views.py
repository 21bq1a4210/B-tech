from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# req --> resp
# req handler
# action



def say_hello(request):
    # Pull data from db
    # Transform data
    #    send emails

    #return HttpResponse('Hello World')
    return render(request, 'home.html', {'name': 'Sarath'})