from django.shortcuts import render, redirect
from .models import Employee
from django.contrib import messages

from django.contrib import messages


def index(request):
    if request.method == 'POST':
        empId = request.POST['empId']
        empname = request.POST['empName']
        device_working_condition = True if request.POST['workingCondition'] == 'yes' else False
        device_name = request.POST['deviceName']
        os_version = request.POST['osVersion']
        location = request.POST['location']
        email = request.POST['email']

        try:
            form = Employee(
                empid=empId,
                empname=empname,
                device_name=device_name,
                device_working_condition=device_working_condition,
                os_version=os_version,
                location=location,
                email=email,
            )
            form.save()
            messages.success(request, 'Employee details saved successfully!')
        except Exception as e:
            messages.error(request, f'Error saving employee details: {str(e)}')

    return render(request, 'index.html')

def search(request):
    if request.method == 'POST':
        # Use request.POST.get() to avoid MultiValueDictKeyError
        type_value = request.POST.get('type')
        query = request.POST.get('search')

        if query is not None and type_value is not None:
            if type_value == 'empid':
                employee_data = Employee.objects.filter(empid=query)
            elif type_value == 'empname':
                employee_data = Employee.objects.filter(empname=query)
            elif type_value == 'device_working_condition':
                employee_data = Employee.objects.filter(device_working_condition=query)
            elif type_value == 'os_version':
                employee_data = Employee.objects.filter(os_version=query)
            elif type_value == 'location':
                employee_data = Employee.objects.filter(location=query)
            elif type_value == 'device_name':
                employee_data = Employee.objects.filter(device_name=query)
            else:
                # Handle the case where an unsupported type is provided
                employee_data = None
        else:
            # Handle the case where 'query' or 'type' is not present in POST data
            employee_data = None

        context = {
            'type_value': type_value,
            'query': query,
            'employee_data': employee_data,
        }

        return render(request, 'search.html', context)

    return render(request, 'search.html')
