# -*- coding: utf-8 -*-

"""Movies views."""

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, filters
from moviesapp.movies.serializers import UserSerializer, GroupSerializer, MovieSerializer, ReviewSerializer
from .models import Movie, Review
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Movie.objects.all().order_by('-year', '-rating')
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title', 'rating', 'year', 'rated', 'released_on', 'genre', 'director']

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

class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviews to be viewed or edited.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
