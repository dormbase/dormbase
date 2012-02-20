from django.db import models
from django.contrib.auth.models import User as AuthUser

class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name    

class Movie(models.Model):
    title = models.CharField(max_length=128) # Title is the one field I consider mandatory.
    year = models.IntegerField(null = True, blank=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    plot = models.CharField(max_length=256, blank=True) 
    plotOutline = models.CharField(max_length=256, blank=True)
    genres = models.ManyToManyField(Genre) # Can link to multiple genres
    mpaa = models.CharField(max_length=128, blank=True)
    runtimes = models.CharField(max_length=3, blank=True)
    coverUrl = models.URLField(max_length=256, blank=True)
    imdbId = models.CharField(max_length=32)
    dateAdded = models.DateField(auto_now_add = True) # To track new films. 
    

    available = models.BooleanField(default=True)
    checkedOutBy = models.ForeignKey(AuthUser, null = True, blank = True) # Not totally sure how this plays with AuthUser yet.
    checkedOutSince = models.DateField(null = True, blank = True) # Can this be left unintialied?


    title = models.CharField(max_length=128)
    year = models.CharField(max_length=4)
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    plot = models.CharField(max_length=256) 
    plotOutline = models.CharField(max_length=256)
    genres = models.ManyToManyField(Genre) # Can link to multiple genres
    mpaa = models.CharField(max_length=50)
    runtimes = models.CharField(max_length=3)
    coverUrl = models.CharField(max_length=128)
   
    def __unicode__(self):
        return self.title
