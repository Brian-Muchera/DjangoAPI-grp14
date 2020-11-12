from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.response import Response
from rest_framework import status 

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
    
    # def put(self,request,pk=None):
    #     return self.update(request,pk)
       
    def put(self, request, format=None):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk=None):
        pk = self.kwargs.get('pk')        
        patients_delete = Patient.objects.filter(pk = pk)
        patients_delete.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

