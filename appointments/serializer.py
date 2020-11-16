from . models import Appointments
from rest_framework import serializers
from rest_framework import routers, serializers, viewsets



class AppointmentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Appointments
        fields=('patient','doctor', 'date','time_alloted','is_completed','is_confirmed','is_rejected','is_confirmed','created_at','updated_at')