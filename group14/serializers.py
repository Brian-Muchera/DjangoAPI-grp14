from rest_framework import serializers
from .models import Patient,Doctor,User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()

class PatientRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
 
    class Meta:
        model = Patient
        fields = ['id','first_name', 'last_name', 'email', 'phone', 'password', 'age','address', 'date_of_birth']
 
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
        fields = ['id','first_name', 'last_name', 'email', 'password', 'qualification','speciality']
 
    def create(self, validated_data):
        return Doctor.objects.create_doctor(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)
    is_user_doctor = serializers.BooleanField(read_only=True)
    is_user_patient = serializers.BooleanField(read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Wrong email or password.")
        is_doctor = user.is_doctor
        is_patient = user.is_patient
        data["refresh_token"] = RefreshToken.for_user(user)
        data["access_token"] = RefreshToken.for_user(user).access_token
        data["is_user_doctor"] = is_doctor
        data["is_user_patient"] = is_patient
        return data