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
    MEMBERSHIP_BRONZE = 'B' #makes easy to change in the feature
    MEMBERSHIP_SILVER = 'S' #makes easy to change in the feature
    MEMBERSHIP_GOLD = 'G' #makes easy to change in the feature

    MEMBERSHIP_CHOICE = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICE, default=MEMBERSHIP_BRONZE)

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICE = [
        PAYMENT_STATUS_PENDING, 'Pending',
        PAYMENT_STATUS_COMPLETE, 'Complete',
        PAYMENT_STATUS_FAILED, 'Failed'
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICE, default=PAYMENT_STATUS_PENDING)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    