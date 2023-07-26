from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
# Create your views here.
# req --> resp
# req handler
# action

def say_hello(request):
    # Pull data from db
    # Transform data
    #    send emails
    query_set = Product.objects.all()
    # for product in query_set:
    #     print(product)
    # list(query_set)
    #  query_set[0]
    # query_set.filter().filter().order_by()
    
    #return HttpResponse('Hello World')
    return render(request, 'home.html', {'name': 'Sarath'})