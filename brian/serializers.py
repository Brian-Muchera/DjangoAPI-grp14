from rest_framework import serializers
from group14.models import Doctor,Patient,User
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['name', 'qualification', 'speciality', 'profile_picture', 'bio', 'address', 'contact']


class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'profile_picture', 'bio', 'address', 'contact']







        