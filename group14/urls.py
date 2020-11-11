from . import views 
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from group14.views import AppointmentsList



urlpatterns = [

    
    url(r'^api/appointments/$', views.AppointmentsList.as_view())
]