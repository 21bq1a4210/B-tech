from django import forms
from .models import Employee

class YourForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
