"""
API V1: Movie Default Serializers
"""
###
# Libs
###
from rest_framework import serializers

from app.movie.models.movie import Movie


###
# Serializer

class DefaultMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
