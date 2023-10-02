from django.contrib import admin

# Register your models here.
# from .models import Grievance, GrievanceMember, College, Complainant, Department
#
# admin.site.register(Grievance)
# admin.site.register(GrievanceMember)
# admin.site.register(College)
# admin.site.register(Complainant)
# admin.site.register(Department)
from django.contrib import admin
from .models import Grievance

admin.site.register(Grievance)
