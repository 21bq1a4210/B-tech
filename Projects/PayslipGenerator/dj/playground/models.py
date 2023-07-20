from django.db import models
from djongo import models

class Employee(models.Model):
    employee_name= models.CharField(max_length=100)
    employee_id= models.CharField(max_length=20).primary_key
    employee_degigntion=models.CharField(max_length=50)
    employee_dept=models.CharField(max_length=50)
    employee_mail=models.EmailField
class Employee_pdf(models.Model):
    employee_id=models.CharField(max_length=20)
    employee_payslip_dir=models.CharField(max_length=255)



                                
