from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.say_hello, name='say_hello'),
    path('loginpg/', views.login_page, name='lgpage'),
    path('login/', views.login_user, name='login'),
]

'''
path('hello/', views.say_hello, name='say_hello'),
1: hello/ -> example.com/hello/ 
2: say_hello -> calling the say_hello method from view.py
'''