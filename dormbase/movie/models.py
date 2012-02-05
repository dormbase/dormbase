from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name    

class Movie(models.Model):
    title = models.CharField(max_length=128)
    year = models.CharField(max_length=4, blank=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    plot = models.CharField(max_length=256, blank=True) 
    plotOutline = models.CharField(max_length=256, blank=True)
    genres = models.ManyToManyField(Genre) # Can link to multiple genres
    mpaa = models.CharField(max_length=50, blank=True)
    runtimes = models.CharField(max_length=3, blank=True)
    coverUrl = models.CharField(max_length=128, blank=True)
   
    def __unicode__(self):
        return self.title
