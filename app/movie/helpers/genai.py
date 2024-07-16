###
# Libs
###
import google.generativeai as genai
import json

from settings.settings import GOOGLE_API_KEY


genai.configure(api_key=GOOGLE_API_KEY)


###
# Genai Ask fuction
###
def get_movie_suggestion(genre, type):

    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(f"Baseado no gênero: {genre} e no tipo de filme descrito: {type}, "
                                      "forneça detalhes completos de um filme com título, descrição, data de lançamento, "
                                      "gênero e classificação. Responda no formato JSON com as chaves: "
                                      "'title', 'description', 'release_date', 'genre', 'rating'. "
                                      "A data de lançamento deve estar no formato AAAA-MM-DD e a classificação deve ser um número flutuante.")

    response_details_clean = response.text.strip().strip('```json').strip('```')

    movie_dict = json.loads(response_details_clean)
    return movie_dict
