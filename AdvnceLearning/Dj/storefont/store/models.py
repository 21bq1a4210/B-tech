from django.db import models

# Create your models here.
class Product(models.Model):
    # Dj model field types: https://docs.djangoproject.com/en/4.2/ref/models/fields/
    
    title = models.CharField(max_length=255) #varchar(255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2) #ex: 9999.99
    inventory = models.IntegerField()
    last_pudate = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
