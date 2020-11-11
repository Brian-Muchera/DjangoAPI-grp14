from django.shortcuts import render
from .models import Appointments
from django.shortcuts import get_object_or_404
from django.contrib import messages

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import AppointmentsSerializer

# Create your views here.

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

class AppointmentsList(APIView):
    def get(self, request, format=None):
        all_appointments = AppointmentsSerializer.objects.all()
        serializers = AppointmentsSerializer(all_appointments, many=True)
        return Response(serializers.data)