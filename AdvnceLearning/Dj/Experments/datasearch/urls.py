from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search')
]
'''
path('hello/', views.say_hello, name='say_hello'),
1: hello/ -> example.com/hello/ 
2: say_hello -> calling the say_hello method from view.py
'''