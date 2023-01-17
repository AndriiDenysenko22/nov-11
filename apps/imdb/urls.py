from django.urls import path

from apps.imdb.views import MovieListView

app_name = 'imdb'


urlpatterns = [
    path('', MovieListView.as_view())
]
