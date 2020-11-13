
from django.conf import settings
from rest_framework import response
from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from group14.views import PatientRegistration,DoctorRegistration,UserLogin




urlpatterns=[
    path('register/patient/', views.PatientRegistration.as_view(),name='register_patient'),
    path('register/doctor/', views.DoctorRegistration.as_view(),name='register_doctor'),
    path('user/',views.UserLogin.as_view(),name='user_login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
    
    