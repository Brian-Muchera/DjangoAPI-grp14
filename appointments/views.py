from django.shortcuts import render
from .models import Appointments
from rest_framework import status

from rest_framework import viewsets
# from rest_framework import permissions

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import AppointmentsSerializer

from rest_framework import mixins
from rest_framework import generics


# Create your views here.

class AppointmentsList(APIView):

    queryset = Appointments.objects.all()
    serializer_class = AppointmentsSerializer
    # permission_classes = (permissions.IsAuthenticated,)


    """
    List all appointments, or create a new appointments.
    """
    def get(self, request, format=None):
        appointments = Appointments.objects.all()
        serializer = AppointmentsSerializer(appointments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AppointmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        pk = self.kwargs.get('pk')
        # appointments = self.get_object(pk)
        appointments = Appointments.objects.filter(pk = pk)
        appointments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, format=None):
        serializer = AppointmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
