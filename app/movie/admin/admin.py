"""
Movie admin
"""
###
# Libs
###
from django.contrib import admin

from app.movie.models.movie import Movie


###
# Inline Admin Models
###


###
# Main Admin Models
###


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )


admin.site.register(Movie, MovieAdmin)
