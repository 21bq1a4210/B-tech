from django.urls import path
from . import views

urlpatterns = [
    path('grievance_form/', views.grievance_form, name='grievance_form'),
    path('success_page/', views.success_page, name='success_page'),  # Define this view
]