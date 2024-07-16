###
# Libs
###
from django.apps import AppConfig


###
# Config
###
class MovieConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.movie'
    
    def ready(self):
        import app.movie.signals
