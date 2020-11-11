from . import views 
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from group14.views import update_bookings,delete_bookings



urlpatterns = [

    url(r'^patients/(?P<id>\d+)/$', views.update_bookings, name='update_bookings'),
    url(r'^patients/(?P<id>\d+)/delete$', views.delete_bookings, name='delete_bookings'),
    url(r'^api/appointments/$', views.AppointmentsList.as_view())
]