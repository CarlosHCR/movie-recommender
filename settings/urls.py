"""
Root URL Configuration
"""
###
# Libs
###
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger Config
schema_view = get_schema_view(
    openapi.Info(
        title="Movie Recommender API",
        default_version='v1',
        description="Movie Recommender Backend",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [

    # Admin CRM
    path('admin/', admin.site.urls),

    # App
    path('', include('app.movie.urls')),

    # Swagger urls
    path('swagger', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
]
