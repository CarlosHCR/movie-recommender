"""
API V1: Movie Create Serializers
"""
###
# Libs
###
from rest_framework import serializers

from app.movie.models.movie import Movie
from app.movie.helpers.genai import get_movie_suggestion


###
# Serializer
###

class CreateMovieSerializer(serializers.ModelSerializer):

    type = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = Movie
        fields = ['genre', 'type']

    def create(self, validated_data):
        genre = validated_data['genre']
        type_description = validated_data['type']

        movie_details = get_movie_suggestion(genre, type_description)

        return Movie.objects.create(
            title=movie_details['title'],
            description=movie_details['description'],
            release_date=movie_details['release_date'],
            genre=movie_details['genre'],
            rating=movie_details['rating']
        )
