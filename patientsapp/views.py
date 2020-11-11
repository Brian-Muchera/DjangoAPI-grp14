from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer

# Create your views here.
class PatientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get(self,request,pk=None):

        if pk:
            return self.retrieve(request)
        else:
            return self.PatientView(request)
  
    def post(self,request):
        return self.create(request)
    
    def put(self,request,pk=None):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)


