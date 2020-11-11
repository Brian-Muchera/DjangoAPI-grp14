from django.db import models
# from uuidfield import UUIDField
from django.urls import reverse

# Create your models here.

class Appointments(models.Model):

    appointments_id=models.IntegerField()
    patients_id=models.CharField(max_length=100)
    doctor_id=models.CharField(max_length=100)
    date=models.CharField(max_length=50)
    time_alloted=models.CharField(max_length=50)
    is_completed=models.BooleanField(default=False)
    is_confirmed=models.BooleanField(default=False)
    is_rejected=models.BooleanField(default=False)
    is_disabled=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        get_latest_by='created_at'

        # appointments_id, created_at, date, doctor_id, id, is_completed, is_confirmed, is_disabled, is_rejected, patients_id, time_alloted, updated_at
