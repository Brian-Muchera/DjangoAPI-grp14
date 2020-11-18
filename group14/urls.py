
from django.conf import settings
from rest_framework import response
from django.urls import path,include
from . import views

from group14.views import PatientRegistration,DoctorRegistration




urlpatterns=[
    path('register/patient/', views.PatientRegistration.as_view(),name='register_patient'),
    path('register/doctor/', views.DoctorRegistration.as_view(),name='register_doctor'),
    path('login/user/', views.LoginAPIView.as_view(), name='login'),
]
    
    