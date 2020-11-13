from . import views 
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from appointments.views import AppointmentsList
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    # path('appointments/', views.appointments_list),
    # path('appointments/<int:pk>/', views.appointments_detail),
   
    # path('appointments/<int:pk>/', views.AppointmentsDetail.as_view()),
    path('appointments/', views.AppointmentsList.as_view()),
    url('^api/appointments/$', views.AppointmentList.as_view()),
    url(r'^appointments/(?P<pk>[0-9]+)/',AppointmentsList.as_view())
    # url(r'^api/appointments/$', views.AppointmentsViewSet),


]
urlpatterns = format_suffix_patterns(urlpatterns)