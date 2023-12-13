from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='lgpage'),
    path('hello/', views.say_hello, name='say_hello'),
    path('login/', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register')
]
'''
path('hello/', views.say_hello, name='say_hello'),
1: hello/ -> example.com/hello/ 
2: say_hello -> calling the say_hello method from view.py
'''