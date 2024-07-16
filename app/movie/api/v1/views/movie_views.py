"""
API V1: Movie Views
"""
###
# Libs
###
from rest_framework import viewsets

from app.movie.models.movie import Movie
from app.movie.api.v1.serializers.movie.create import CreateMovieSerializer
from app.movie.api.v1.serializers.movie.default import DefaultMovieSerializer


###
# Viewsets
###
class MovieViewSet(viewsets.ModelViewSet):

    serializer_class = DefaultMovieSerializer
    queryset = Movie.objects.all().order_by('id')
    permission_classes = []

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateMovieSerializer
        return DefaultMovieSerializer

