from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from .views import ProfileViewSet
from . import views 


router = routers.DefaultRouter()
router.register(r'profile', views.ProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]