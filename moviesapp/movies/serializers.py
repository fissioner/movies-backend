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
    rating = serializers.SerializerMethodField('get_rating')
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = ['url', 'id', 'title', 'poster', 'rating', 'year', 'rated', 'released_on', 'genre', 'director', 'plot', 'reviews']

    def get_rating(self, obj):
        rating = obj.get_rating()
        return rating