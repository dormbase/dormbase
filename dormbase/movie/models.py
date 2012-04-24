# Dormbase -- open-source dormitory database system
# Copyright (C) 2012 Alex Chernyakhovsky <achernya@mit.edu>
#                    Drew Dennison       <dennison@mit.edu>
#                    Isaac Evans         <ine@mit.edu>
#                    Luke O'Malley       <omalley1@mit.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
        return unicode(self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('dormbase.movie.views.movie_detail', (), {
                'movieId': self.imdbId })
    
