from . models import Appointments
from rest_framework import serializers
from rest_framework import routers, serializers, viewsets



class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointments
        fields=('patient','doctor', 'date','time_alloted')