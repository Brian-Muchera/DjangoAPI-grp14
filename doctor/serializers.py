from rest_framework import serializers
from doctor.models import Doctor

class DoctorSerializer(serializers.Serializer):
    class Meta:
        model = Doctor
        fields = ('doctor_id',
                   'doctorName',
                   'speciality',
                   'city',
                   'phoneNumber')