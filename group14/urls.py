from django.conf.urls import url
from group14 import views

urlpatterns=[ 
    url(r'^doctor/$',views.doctorApi),
    url(r'^doctor/([0-9]+)$',views.doctorApi),
]