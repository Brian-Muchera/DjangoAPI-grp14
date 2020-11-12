# -*- coding: utf-8 -*-
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response


# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer