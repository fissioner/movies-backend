from django.contrib.auth.models import User, Group
from rest_framework import serializers
from moviesapp.movies.models import Movie, Review
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password", )


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