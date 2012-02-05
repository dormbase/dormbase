from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name    

class Movie(models.Model):
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
