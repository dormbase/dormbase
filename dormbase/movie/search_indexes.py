from haystack import indexes
from haystack import site
from dormbase.movie.models import *

class MovieIndex(indexes.SearchIndex):
    text = indexes.EdgeNgramField(document=True, use_template=True)

    def get_model(self):
        return Movie

    def index_queryset(self):
        return self.get_model().objects

site.register(Movie, MovieIndex)
