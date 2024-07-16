###
# Libs
###
from django.test import TestCase
from unittest.mock import patch
from datetime import date

from app.movie.api.v1.serializers.movie.create import CreateMovieSerializer


###
# Test Create Movie Serializer
###
class CreateMovieSerializerTest(TestCase):

    @patch('app.movie.api.v1.serializers.movie.create.get_movie_suggestion')
    def test_create_movie_serializer(self, mock_get_movie_suggestion):
        mock_movie_data = {
            'title': 'Test Movie',
            'description': 'Test description',
            'release_date': date(2024, 1, 1),
            'genre': 'Test genre',
            'rating': 8.5
        }
        mock_get_movie_suggestion.return_value = mock_movie_data

        data = {'genre': 'Test genre', 'type': 'Test type'}
        serializer = CreateMovieSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        movie = serializer.save()

        self.assertEqual(movie.title, mock_movie_data['title'])
        self.assertEqual(movie.description, mock_movie_data['description'])
        self.assertEqual(movie.release_date, mock_movie_data['release_date'])
        self.assertEqual(movie.genre, mock_movie_data['genre'])
        self.assertEqual(movie.rating, mock_movie_data['rating'])
