from django.shortcuts import render
from .models import Appointments
from rest_framework import status

from rest_framework import viewsets
from rest_framework import permissions

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import AppointmentsSerializer

from rest_framework import mixins
from rest_framework import generics


# Create your views here.

class AppointmentsList (APIView):

    queryset = Appointments.objects.all()
    serializer_class = AppointmentsSerializer


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

def patient_book_appointment_view(request):
    appointmentForm=forms.PatientAppointmentForm()
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    mydict={'appointmentForm':appointmentForm,'patient':patient}
    if request.method=='POST':
        appointmentForm=forms.PatientAppointmentForm(request.POST)
        if appointmentForm.is_valid():
            appointment=appointmentForm.save(commit=False)
            appointment.doctorId=request.POST.get('doctorId')
            #appointment.patientId=request.user.id #----user can choose any patient but only their info will be stored
            appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
            #appointment.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
            appointment.status=False
            appointment.save()
        return HttpResponseRedirect('patient-view-appointment')
    return redirect ('index')

class AppointmentList(APIView):
    def get(self, request, format=None):
        all_appointments = Appointments.objects.all()
        serializers = AppointmentsSerializer(all_appointments, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = AppointmentsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors)
    def delete(self, request, pk=None):
        pk = self.kwargs.get('pk')
        # appointments = self.get_object(pk)
        appointments = Appointments.objects.filter(pk = pk)
        appointments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)