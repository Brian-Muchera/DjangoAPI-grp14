from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from group14.models import Doctor
from group14.serializers import DoctorSerializer

# Create your views here.
@csrf_exempt
def doctorApi(request,id=0):
    if request.method=='GET':
        doctors = Doctor.objects.all()
        doctors_serializer = DoctorSerializer(doctors, many=True)
        return JsonResponse(doctors_serializer.data, safe=False)

    elif request.method=='POST':
        doctor_data = JSONParser().parse(request)
        doctor_serializer = DoctorSerializer(data=doctor_data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse("Doctor Added Successfully", safe=False)
        return JsonResponse("Failed to add doctor", safe=False)

    elif request.method=='PUT':
        doctor_data = JSONParser().parse(request)
        doctor=Doctor.objects.get(doctor_id=doctor_data['doctor_id'])
        doctor_serializer=DoctorSerializer(doctor,data=doctor_data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse("Doctor Updated Successfully", safe=False)
        return JsonResponse("Failed to update doctor", safe=False)

    elif request.method=='DELETE':
        doctor=Doctor.objects.get(doctor_id=id)
        doctor.delete()
        return JsonResponse("Deleted Successfully", safe=False)


