# import jwt
from django.conf import settings
from django.shortcuts import render
from rest_framework import authentication, exceptions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Doctor, Patient
from .serializers import (DoctorRegistrationSerializer,
                          PatientRegistrationSerializer)


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
 


