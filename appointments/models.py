from django.db import models
# from uuidfield import UUIDField
from django.urls import reverse
from group14.models import Doctor,Patient
# Create your models here.

class Appointments(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, max_length=100)
    doctor = models.ForeignKey( Doctor, on_delete=models.CASCADE)
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