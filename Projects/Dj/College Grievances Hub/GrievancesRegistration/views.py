# from django.shortcuts import render
# from django.shortcuts import HttpResponse
# # Create your views here.
# # def index(request):
# #     return HttpResponse("Welcome to the GrievancesRegistration home page")
#
# def grievancesRegestrationForm(request):
#      return render(request, "index.html")

from django.shortcuts import render, redirect, HttpResponse
from .models import Grievance
from .send_mail import SendMail

def grievance_form(request):
    if request.method == 'POST':
        complaintant_name = request.POST['complaintant_name']
        registration_no = request.POST['registration_no']
        email = request.POST['email']
        who = request.POST['who']
        dept = request.POST['dept']
        year = request.POST['year']
        g = request.POST['g']
        Grevience_column = request.POST['Grevience_column']

        grievance = Grievance(
            complaintant_name=complaintant_name,
            registration_no=registration_no,
            email=email,
            who=who,
            dept=dept,
            year=year,
            g=g,
            Grevience_column=Grevience_column
        )
        grievance.save()

        #last_record = Grievance.objects.latest('-id')

        data = {
            'id' : grievance.id,
            'name' : grievance.complaintant_name,
            'reg_number' : grievance.registration_no,
            'email' : grievance.email,
            'who' : grievance.who,
            'dept': grievance.dept,
            'year': grievance.year,
            'type_of_grievance': grievance.g,
            'complant': grievance.Grevience_column
        }

        # MailToCounseller(data
        mail = SendMail(data)
        mail.MailToCounseller()

        # You can redirect to a success page or do any other desired action here.
        return redirect('success_page')

    return render(request, 'index.html')

def success_page(request):
    # You can customize this view as needed, and render the success page template.
    return HttpResponse("Succesfull submited")
