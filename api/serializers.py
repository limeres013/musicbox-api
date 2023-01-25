from .models import Artist

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username']
            )
        ]

class ArtistSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(max_length=120)
    carreer_start_date = serializers.DateField()
    place_of_origin = serializers.CharField(max_length=200)

    def create(self, data):
        artist = Artist.objects().create_artist(**data)
        return artist

    class Meta:
        model = Artist
        fields = (
            'artist_name',
            'carreer_start_date',
            'place_of_origin',
        )