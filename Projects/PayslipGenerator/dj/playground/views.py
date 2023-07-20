from django.shortcuts import render
from django.http import HttpResponse
from .forms import upload
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from generator import views
import pandas as pd
fs=FileSystemStorage()
def say_hello(request):
    return render(request, 'hello.html')
@csrf_exempt
def upload_file(request):
    import pythoncom
    pythoncom.CoInitialize()
    global data
    if request.method == 'POST':
        form = upload(request.POST,request.FILES)
        file = request.FILES.get('file')
        data=pd.read_excel(file)
        views.pdfgenerator()
        return HttpResponse("pdf files are succesfully generated")
        
    else:
        form=upload()
    return render(request, 'upload.html')
    pythoncom.CoUninitialize()
    
def exceldata():
    return data