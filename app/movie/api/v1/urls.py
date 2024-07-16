"""
API V1: Movie Urls
"""
###
# Libs
###
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.movie.api.v1.views.movie_views import MovieViewSet


###
# Routers
###
""" Main router """
router = DefaultRouter()

router.register(
    r'movie',
    MovieViewSet,
    basename='movie'
)

###
# URLs
###
urlpatterns = [
    path('', include(router.urls)),
]
