###
# Libs
###
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import date
from unittest.mock import patch

from app.movie.models.movie import Movie


###
# Test Movie ViewSet
###
class MovieViewSetTest(APITestCase):

    @patch('app.movie.api.v1.serializers.movie.create.get_movie_suggestion')
    def test_create_movie(self, mock_get_movie_suggestion):
        mock_movie_data = {
            'title': 'Test Movie',
            'description': 'Test description',
            'release_date': date(2024, 1, 1),
            'genre': 'Test genre',
            'rating': 8.5
        }
        mock_get_movie_suggestion.return_value = mock_movie_data

        url = reverse('movie-list')
        data = {'genre': 'Test genre', 'type': 'Test type'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 1)
        movie = Movie.objects.get()

        self.assertEqual(movie.title, mock_movie_data['title'])
        self.assertEqual(movie.description, mock_movie_data['description'])
        self.assertEqual(movie.release_date, mock_movie_data['release_date'])
        self.assertEqual(movie.genre, mock_movie_data['genre'])
        self.assertEqual(movie.rating, mock_movie_data['rating'])
