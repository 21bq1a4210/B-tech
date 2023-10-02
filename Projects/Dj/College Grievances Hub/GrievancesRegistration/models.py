from django.db import models

class Grievance(models.Model):
    complaintant_name = models.CharField(max_length=100)
    registration_no = models.CharField(max_length=20)
    email = models.EmailField()
    who = models.CharField(max_length=10, choices=[('student', 'Student'), ('faculty', 'Faculty')])
    dept = models.CharField(max_length=10, choices=[('cse', 'CSE'), ('csm', 'CSM'), ('cic', 'CIC'), ('cso', 'CSO'), ('it', 'IT'), ('mech', 'MECH'), ('civil', 'CIVIL'), ('aiml', 'AIML'), ('EEE', 'EEE'), ('ECE', 'ECE'), ('AIDS', 'AIDS')])
    year = models.IntegerField(choices=[(1, '1st year'), (2, '2nd year'), (3, '3rd year'), (4, '4th year')])
    g = models.CharField(max_length=20, choices=[('academic', 'Academic'), ('non-academic', 'Non-Academic'), ('discrimination', 'Discrimination')])
    Grevience_column = models.TextField()

    def __str__(self):
        return self.complaintant_name


# from django.db import models
# # Create your models here.
#
# # Department Model
# class Department(models.Model):
#     department_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     designation_choices = [
#         ('student', 'Student'),
#         ('prof', 'Professor'),
#         ('assoc_prof', 'Associate Professor'),
#         ('asst_prof', 'Assistant Professor'),
#     ]
#     designation = models.CharField(max_length=20, choices=designation_choices, default='student')
#
# # College Model
# class College(models.Model):
#     college_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     address = models.TextField()
#     affiliation_university = models.CharField(max_length=100)
#
# # Complainant Model
# class Complainant(models.Model):
#     complainant_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone_no = models.CharField(max_length=15)
#     complainant_choices = [
#         ('student', 'Student'),
#         ('faculty', 'Faculty'),
#     ]
#     complainant_choice = models.CharField(max_length=10, choices=complainant_choices)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     branch = models.CharField(max_length=100)  # You might need to define this field more clearly
#
# # Grievance Model
# class Grievance(models.Model):
#     grievance_id = models.AutoField(primary_key=True)
#     description = models.TextField()
#     date_occurrence = models.DateTimeField()
#     status_choices = [
#         ('complete', 'Complete'),
#         ('pending', 'Pending'),
#     ]
#     status = models.CharField(max_length=10, choices=status_choices)
#     complainant = models.ForeignKey(Complainant, on_delete=models.CASCADE)
#     grievance_category = models.CharField(max_length=100)  # You should define categories
#
# # Grievance Members Model
# class GrievanceMember(models.Model):
#     grievance_member_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone_no = models.CharField(max_length=15)
#     departments = models.ManyToManyField(Department)