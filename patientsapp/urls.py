from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('patient', views.PatientView)

urlpatterns=[    
    path('', include(router.urls)),  
    
]
