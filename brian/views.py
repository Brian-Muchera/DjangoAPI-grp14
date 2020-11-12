# -*- coding: utf-8 -*-
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework import status


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


    def delete(self, request, pk=None):
        pk = self.kwargs.get('pk')
        profile_delete = Profile.objects.filter(pk = pk)
        profile_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        profile_put = Profile.objects.filter(pk = pk)
        profile_put.put()
        return self.update(request, *args, **kwargs)