from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.contrib.auth.models import User
from doctor.models import Doctor
from doctor.serializers import DoctorSerializer


class DoctorView(APIView):
    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, *args, **kwargs):
        doctors = get_object_or_404(Doctor, pk=kwargs['doctor_id'])
        serializer = DoctorSerializer(doctors)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        doctor = get_object_or_404(Doctor, pk=kwargs['doctor_id'])
        serializer = DoctorSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            doctor = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')        
        doctor_delete = Doctor.objects.filter(pk = pk)
        doctor_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


