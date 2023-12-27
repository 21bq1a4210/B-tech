from django.shortcuts import render, redirect

def index_pg(request):
    if request.method == 'POST':
        print('in post')
        img = request.FILES.get('img')
        print('File uploaded:', img.name)
    return render(request, 'image_uplode.html')

