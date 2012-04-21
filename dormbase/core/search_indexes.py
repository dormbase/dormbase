from haystack import indexes
from haystack import site
from dormbase.core.models import *

class ResidentIndex(indexes.SearchIndex):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    
    def get_model(self):
        return Resident

    def index_queryset(self):
        return self.get_model().objects

site.register(Resident, ResidentIndex)
