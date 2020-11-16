from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from rest_framework import response
from .views import DoctorProfile,PatientProfile
from . import views 



urlpatterns = [
    path('profile/doctor', views.DoctorProfile.as_view(),name='doctor_profile'),
    path('profile/patient', views.PatientProfile.as_view(),name='patient_profile'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]