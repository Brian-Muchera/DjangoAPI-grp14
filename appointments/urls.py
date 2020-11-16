from . import views 
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from appointments.views import AppointmentsList
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('appointments/', views.AppointmentsList.as_view(),name='appointments'),
    path('appointments/<pk>/',AppointmentsList.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)