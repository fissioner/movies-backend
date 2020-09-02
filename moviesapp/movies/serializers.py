from django.contrib.auth.models import User, Group
from rest_framework import serializers
from moviesapp.movies.models import Movie, Review


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ['url', 'name']


class ReviewSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Movie
        fields = ['url', 'id', 'title', 'year', 'released_on', 'genre', 'director', 'plot', 'created_at', 'updated_at']