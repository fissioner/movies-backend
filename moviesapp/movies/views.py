# -*- coding: utf-8 -*-

"""Movies views."""

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from moviesapp.movies.serializers import UserSerializer, GroupSerializer, MovieSerializer
from .models import Movie


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Movie.objects.all().order_by('-year') # '-rating'
    serializer_class = MovieSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
