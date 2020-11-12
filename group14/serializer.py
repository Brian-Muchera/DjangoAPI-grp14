from rest_framework import serializers
from group14.models import Doctor

class DoctorSerializer(serializers.Serializer):
    class Meta:
        model = Doctor
        fields = ('doctor_id',
                   'doctorName',
                   'speciality',
                   'city',
                   'phoneNumber')