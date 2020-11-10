from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from rest_framework import routers
from .views import ProfileViewSet
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from group14.views import update_bookings,delete_bookings

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)



urlpatterns = [
    url(r'^viewset/',include(router.urls)),
    url(r'^$',views.home,name='home'),
    url(r'^profile/(?P<id>\d+)/$', views.Profile, name='prof'),
    url(r'^patients/(?P<id>\d+)/$', views.update_bookings, name='update_bookings'),
    url(r'^patients/(?P<id>\d+)/delete$', views.delete_bookings, name='delete_bookings'),

]