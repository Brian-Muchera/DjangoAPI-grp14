from django.db import models
#
# Create your models here.
class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctorName = models.CharField(max_length=100)
    speciality =  models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)