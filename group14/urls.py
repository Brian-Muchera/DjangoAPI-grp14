from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers
from .views import ProfileViewSet

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)
from . import views 
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from group14.views import update_bookings,delete_bookings



urlpatterns = [
    url(r'^viewset/',include(router.urls)),
    url(r'^$',views.home,name='home'),
    url(r'^profile/',views.Profile),

    url(r'^patients/(?P<id>\d+)/$', views.update_bookings, name='update_bookings'),
    url(r'^patients/(?P<id>\d+)/delete$', views.delete_bookings, name='delete_bookings'),

]