###
# Libs
###
from django.test import TestCase
from unittest.mock import patch

import app.movie.helpers.genai as genai_helper


###
# Test GenAI Helper
###
class GetMovieSuggestionTest(TestCase):

    @patch('app.movie.helpers.genai.genai.GenerativeModel')
    def test_get_movie_suggestion(self, mock_generative_model):
        mock_response = mock_generative_model.return_value.generate_content.return_value
        mock_response.text = '{ \
            "title": "Mock Movie",\
            "description": "Mock description",\
            "release_date": "2024-01-01",\
            "genre": "Mock Genre",\
            "rating": 7.5\
        }'

        genre = 'Comedy'
        type_description = 'Family'
        result = genai_helper.get_movie_suggestion(genre, type_description)

        self.assertEqual(result['title'], 'Mock Movie')
        self.assertEqual(result['description'], 'Mock description')
        self.assertEqual(result['release_date'], '2024-01-01')
        self.assertEqual(result['genre'], 'Mock Genre')
        self.assertEqual(result['rating'], 7.5)
