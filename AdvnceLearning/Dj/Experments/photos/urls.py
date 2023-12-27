from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_pg, name='uploader_pg'),
]
