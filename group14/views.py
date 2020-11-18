from django.conf import settings
from django.shortcuts import render
from rest_framework import authentication, exceptions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Doctor, Patient,User
from .serializers import (DoctorRegistrationSerializer,
                          PatientRegistrationSerializer)
from rest_framework import viewsets

class PatientRegistration(APIView):
    permission_classes = (AllowAny,)
    serializer_class = PatientRegistrationSerializer
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, format=None):
        patients = Patient.objects.all()
        serializer = PatientRegistrationSerializer(patients, many=True)
        return Response(serializer.data)
class DoctorRegistration(APIView):
    permission_classes = (AllowAny,)
    serializer_class = DoctorRegistrationSerializer
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        doctors = Doctor.objects.all()
        serializer = DoctorRegistrationSerializer(doctors, many=True)
        return Response(serializer.data)