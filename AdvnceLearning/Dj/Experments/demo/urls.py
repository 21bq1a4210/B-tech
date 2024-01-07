from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('demo/', views.demo, name='demo'),
    path('ap/', views.ap),
    #path('contact/', views.contact, name='contact'),
    # Add more paths as needed for your application
]
