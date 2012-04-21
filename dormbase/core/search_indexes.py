from haystack import indexes
from haystack import site
from dormbase.core.models import *

class ResidentIndex(indexes.SearchIndex):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    # We add this for autocomplete.
    #athena_username = indexes.EdgeNgramField(model_attr='athena')
    #first_name = indexes.EdgeNgramField(model_attr='user__first_name')
    
    def get_model(self):
        return Resident

    def index_queryset(self):
        return self.get_model().objects

site.register(Resident, ResidentIndex)
