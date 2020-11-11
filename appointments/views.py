from django.shortcuts import render
from .models import Appointments
from rest_framework import status

from rest_framework import viewsets
from rest_framework import permissions

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import AppointmentsSerializer

# Create your views here.

class AppointmentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Appointments to be viewed or edited.
    """
    queryset = Appointments.objects.all().order_by('-created_at')
    serializer_class = AppointmentsSerializer
    permission_classes = [permissions.IsAuthenticated]

    @api_view(['GET', 'POST'])
    def appointments_list(request, format=None):

        """
        List all code appointments, or create a new appointments.
        """
        if request.method == 'GET':
            appointments = Appointments.objects.all()
            serializer = AppointmentsSerializer(appointments, many=True)
            # return JsonResponse(appointments.data, safe=False)
            return Response(serializer.data)


        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = AppointmentsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            #     return JsonResponse(serializer.data, status=201)
            # return JsonResponse(serializer.errors, status=400)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @api_view(['GET', 'PUT', 'DELETE'])
    def appointments_detail(request, pk, format=None):
        """
        Retrieve, update or delete a code appointments.
        """
        try:
            appointments = Appointments.objects.get(pk=pk)
        except Appointments.DoesNotExist:
            # return HttpResponse(status=404)
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = AppointmentsSerializer(appointments)
            # return JsonResponse(serializer.data)
            return Response(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = AppointmentsSerializer(appointments, data=data)
            if serializer.is_valid():
                serializer.save()
            #     return JsonResponse(serializer.data)
            # return JsonResponse(serializer.errors, status=400)

                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        elif request.method == 'DELETE':
            appointments.delete()
            # return HttpResponse(status=204)
            return Response(status=status.HTTP_204_NO_CONTENT)