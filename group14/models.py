from django.db import models
#from uuidfield import UUIDField

# Create your models here.

# class Appointments(models.Model):
#     appointments_id=models.UUIDField(auto=True)
#     patients_id=models.CharField(max_length=100)
#     doctor_id=models.CharField(max_length=100)
#     date=models.CharField(max_length=50)
#     # time_allocated=models.CharField(max_length=50)
#     time_alloted=models.CharField(max_length=50)
#     # number_alloted=models.CharField(max_length=50)
#     is_completed=models.BooleanField(default=False)
#     is_confirmed=models.BooleanField(default=False)
#     is_rejected=models.BooleanField(default=False)
#     is_disabled=models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True, editable=False)
#     updated_at=models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['created_at']
#         get_latest_by='created_at'

class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    

