from rest_framework import serializers
from .models import Patient,Doctor,User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


User = get_user_model()

class PatientRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
 
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'email', 'phone', 'password', 'age', 'city','address', 'date_of_birth']
 
    def create(self, validated_data):
        return Patient.objects.create_patient(**validated_data)
 
class DoctorRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
 
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'email', 'password', 'qualification','speciality']
 
    def create(self, validated_data):
        return Doctor.objects.create_doctor(**validated_data)

