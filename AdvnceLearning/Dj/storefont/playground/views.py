from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
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
    #query_set = Product.objects.all()
    # for product in query_set:
    #     print(product)
    # list(query_set)
    #  query_set[0]
    # query_set.filter().filter().order_by()

    '''Object retrieving:
    query_set = Product.objects.get(pk=1) ##primarykey
    .objects.get(field_name)
    .objects.get(pk=0) through an ObjectDoesNotExist (use try block as follows)
    .object.filter(pk=0).first()  # if the queryset is empty the first() will return None
    TO check the existence of object we use .objects.filter(pk=0).exists() returns an boolean value
    '''
    # product = Product.objects.get(pk=1)
    # query_set = Product.objects.filter(pk=0).first()
    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     return render(request, 'home.html', {'name': 'Sarath there is an exception in your code'})
    #return HttpResponse('Hello World')
    return render(request, 'home.html', {'name': 'Sarath'})