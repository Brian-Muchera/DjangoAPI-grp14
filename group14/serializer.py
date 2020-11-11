from . models import Appointments
from rest_framework import serializers



class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointments
        fields=('appointments_id','patient_id','doctor_id','time_alloted','is_completed','is_confirmed','is_rejected','is_confirmed')