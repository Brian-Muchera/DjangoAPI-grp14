
from django.conf import settings
from rest_framework import response
from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from group14.views import PatientRegistration,DoctorRegistration




urlpatterns=[
    path('register/patient/', views.PatientRegistration.as_view(),name='register_patient'),
    path('register/doctor/', views.DoctorRegistration.as_view(),name='register_doctor'),
    path('login/doctor/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/patient/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
    
    