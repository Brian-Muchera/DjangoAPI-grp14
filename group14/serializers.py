from rest_framework import serializers
from group14.models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('doctor_id',
                   'doctorName',
                   'speciality',
                   'city',
                   'phoneNumber')