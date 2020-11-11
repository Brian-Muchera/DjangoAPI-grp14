from django.shortcuts import render
from .models import Appointments
from django.shortcuts import get_object_or_404
from django.contrib import messages
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import AppointmentsSerializer

# Create your views here.


class AppointmentsList(APIView):
    def get(self, request, format=None):
        all_appointments = AppointmentsSerializer.objects.all()
        serializers = AppointmentsSerializer(all_appointments, many=True)
        return Response(serializers.data)