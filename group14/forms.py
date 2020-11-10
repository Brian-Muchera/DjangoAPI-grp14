from django import forms
from .models import Appointments


class AppointmentsForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields=['appointments_id','patients_id','doctor_id','time_alloted','is_completed','is_confirmde','is_rejected','is_disablde','date']
