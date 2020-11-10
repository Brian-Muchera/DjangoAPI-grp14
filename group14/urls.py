from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers
from .views import ProfileViewSet

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)



urlpatterns = [
    url(r'^viewset/',include(router.urls)),
    url(r'^$',views.home,name='home'),
    url(r'^profile/',views.Profile),
]