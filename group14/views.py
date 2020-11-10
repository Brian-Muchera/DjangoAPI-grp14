from django.shortcuts import render
from .models import Appointment
from django.shortcuts import get_object_or_404
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import AppointmentSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.
class AppointmentList(APIView):
    def get(self, request, format=None):
        all_appointments = Appointment.objects.all()
        serializers = AppointmentSerializer(all_appointments, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = AppointmentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required
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

def update_bookings(request, id=None):
    instance=get_object_or_404(Appointments, id=id)
    form = AppointmentsForm(request.POST or None ,instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        messages.success(request,'Successfully saved')

        return redirect ('index')

    context = {
        'instance':instance,
        'form':form
    }

    return render(request,'group14/update_bookings.html', context)


# @login_required(login_url='/login/')
def delete_bookings(request, id=None):
    instance=get_object_or_404(Computer, id=id)
    instance.delete()
    return redirect ('index')
