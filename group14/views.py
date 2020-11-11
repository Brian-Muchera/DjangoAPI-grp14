from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from group14.models import Doctor
from group14.serializers import DoctorSerializer

# Create your views here.
@csrf_exempt
def doctorApi(request,id=0):
    if request.method=='GET':
        doctor = Doctor.objects.all()
        doctor_serializer = DoctorSerializer(doctor, many=True)
        return JsonResponse(doctor_serializer.data, safe=False)