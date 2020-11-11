from . models import Appointments
from rest_framework import serializers
from rest_framework import routers, serializers, viewsets



class AppointmentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Appointments
        fields=('appointments_id','patients_id','doctor_id', 'date','time_alloted','is_completed','is_confirmed','is_rejected','is_confirmed','created_at','updated_at')

        # fields=('appointments_id', 'created_at', 'date', 'doctor_id', 'id', 'is_completed', 'is_confirmed', 'is_disabled', 'is_rejected', 'patients_id', 'time_alloted', 'updated_at')