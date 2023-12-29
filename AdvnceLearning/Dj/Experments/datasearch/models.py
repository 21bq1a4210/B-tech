from django.db import models
from django.utils import timezone


class Employee(models.Model):
    EMPLOYEE_LOCATIONS = (
        ('a', 'Location A'),
        ('b', 'Location B'),
        ('c', 'Location C'),
        ('d', 'Location D'),
    )

    empid = models.CharField(primary_key=True, max_length=255)
    empname = models.CharField(max_length=255)
    device_working_condition = models.BooleanField(default=False)  # Default to No
    device_name = models.CharField(max_length=255, null=True, blank=True)
    os_version = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=1, choices=EMPLOYEE_LOCATIONS)
    email = models.EmailField(null=True)  # Allow null values for email
    submission_time = models.DateTimeField(default=timezone.now)  # New field for submission time


def __str__(self):
        return f"{self.empid} - {self.empname}"
