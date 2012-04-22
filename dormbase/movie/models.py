from django.db import models
from django.contrib.auth.models import User as AuthUser
from photologue.models import Photo

class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name    

class Movie(models.Model):
    title = models.CharField(max_length=128) # Title is the one field I consider mandatory.
    canonicalTitle = models.CharField(max_length=128)
    year = models.IntegerField(null = True, blank=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    plot = models.TextField(blank=True) 
    plotOutline = models.TextField(blank=True)
    genres = models.ManyToManyField(Genre) # Can link to multiple genres
    mpaa = models.CharField(max_length=128, blank=True)
    runtimes = models.CharField(max_length=3, blank=True)
    cover = models.ForeignKey(Photo, null = True)
    imdbId = models.CharField(max_length=2) # Mandatory
    director = models.TextField(blank=True)
    cast = models.TextField(blank=True)

    dateAdded = models.DateField(auto_now_add = True) # To track new films. 
    available = models.BooleanField(default=True)
    checkedOutBy = models.ForeignKey(AuthUser, null = True, blank = True) # Not
                                                                          # totally
                                                                          # sure
                                                                          # how
                                                                          # this
                                                                          # plays
                                                                          # with
                                                                          # AuthUser
                                                                          # yet.
    checkedOutSince = models.DateField(null = True, blank = True) # Can this be left unintialized?
   
    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('dormbase.movie.views.movie_detail', (), {
                'movieId': self.imdbId })
    
