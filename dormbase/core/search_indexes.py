from haystack import indexes
from haystack import site
from dormbase.core.models import *

class ResidentIndex(indexes.SearchIndex):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    firstname = indexes.EdgeNgramField(model_attr='user__first_name')
    lastname = indexes.EdgeNgramField(model_attr='user__last_name')
    title  = indexes.EdgeNgramField(model_attr='title')
    username = indexes.EdgeNgramField(model_attr='athena')
    room = indexes.EdgeNgramField(model_attr='room__number')
    year = indexes.IntegerField(model_attr='year')
    
    def get_model(self):
        return Resident

    def index_queryset(self):
        return self.get_model().objects

site.register(Resident, ResidentIndex)
