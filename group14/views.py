# import jwt
from django.conf import settings
from django.shortcuts import render
from rest_framework import authentication, exceptions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Doctor, Patient,User
from .serializers import (DoctorRegistrationSerializer,
                          PatientRegistrationSerializer,UserLoginSerializer)
from rest_framework import viewsets

class PatientRegistration(APIView):
    permission_classes = (AllowAny,)
    serializer_class = PatientRegistrationSerializer
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
 
class DoctorRegistration(APIView):
    permission_classes = (AllowAny,)
    serializer_class = DoctorRegistrationSerializer
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
 
class UserLogin(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

