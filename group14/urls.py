from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)



urlpatterns = [
    path('', views.index, name='index'),
    path('account/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('<username>/profile', views.user_profile, name='userprofile'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/settings', views.edit_profile, name='edit'),