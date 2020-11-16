from rest_framework import viewsets
from django.shortcuts import render
from group14.models import Doctor,Patient,User
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
from .serializers import (DoctorProfileSerializer,
                          PatientProfileSerializer)

User = settings.AUTH_USER_MODEL



class DoctorProfile(APIView):
    permission_classes = (AllowAny,)
    serializer_class = DoctorProfileSerializer
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
   
    def delete(self, request, pk=None):
        pk = self.kwargs.get('pk')
        doctor_delete = Doctor.objects.filter(pk = pk)
        doctor_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, format=None):
        serializer = DoctorProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    




class PatientProfile(APIView):
    permission_classes = (AllowAny,)
    serializer_class = PatientProfileSerializer
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    
   
    def delete(self, request, pk=None):
        pk = self.kwargs.get('pk')
        patient_delete = Patient.objects.filter(pk = pk)
        patient_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, format=None):
        serializer = PatientProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    