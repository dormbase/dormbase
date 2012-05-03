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

import sys
sys.path.append('../contrib/IMDBpy')
import unicodedata
from imdb import IMDb
from dormbase.movie.models import Genre
from dormbase.movie.models import Movie
from photologue.models import Photo
import urllib2
from cStringIO import StringIO
from django.core.files.base import ContentFile
from django.template.defaultfilters import slugify

try:
    import Image
    import ImageFile
    import ImageFilter
    import ImageEnhance
except ImportError:
    try:
        from PIL import Image
        from PIL import ImageFile
        from PIL import ImageFilter
        from PIL import ImageEnhance
    except ImportError:
        raise ImportError('Unable to import the Python Imaging Library. Please confirm it`s installed and available on your current Python path.')


def import_all_genres():
    genre_list = ['Action', 'Adventure', 'Animation', 'Biography',
                 'Comedy', 'Crime', 'Documentary', 'Drama',
                 'Family', 'Fantasy', 'Film-Noir', 'Game-Show',
                 'History', 'Horror', 'Music', 'Musical',
                 'Mystery', 'News', 'Reality-TV', 'Romance',
                 'Sci-Fi', 'Sport', 'Talk-Show', 'Thriller',
                 'War', 'Western', 'New', 'All'] # List was taken from IMDB genre page. 

    for i in genre_list:
        g = Genre(name = i)
        g.save()

def import_movie(movie_id):
    movie_id = movie_id.strip('\n') # Newline character was preventing the movie table from being searchable by ID.
    data = {'title': '',
            'canonical title': '',
            'year': None,
            'rating': None,
            'plot': '', # IMDB provides list of plots from different contributors. 
            'plot outline': '',
            'genres': '', #IMDB provides list of genres.
            'mpaa': 'Mpaa not available.',
            'runtimes': '',
            'full-size cover url': '',
            'imdbId': movie_id,
            'director': '',
            'cast': '',}
    
    movie = IMDb().get_movie(movie_id)

    title = unicodedata.normalize('NFKD', movie['title']).encode('ascii','ignore')

    for key in data:
        if movie.has_key(key):
            if key == 'director' or key == 'cast':
                plist = [person['name'] for person in movie[key]]
                movie[key] = ', '.join(plist)

            elif type(movie[key]) == type([]) and key != 'genres':
                movie[key] = movie[key][0]
        
            if type(movie[key]) == type(''):
                movie[key] = unicodedata.normalize('NFKD', movie[key]).encode('ascii','ignore')

            data[key] = movie[key]

        elif key != 'imdbId':
                print 'Error! {} not available in {}'.format(key, title)
    cover = None
    try:
        imagedata = urllib2.urlopen(data['full-size cover url']).read()
        cover = Photo(title=data['title'], title_slug = slugify(data['title']))
        cover.image.save(data['imdbId'] + '.jpg', ContentFile(imagedata))
        print "saved an image: " + data['title']
    except Exception as e:
        print "Oh noes, an error"
        print e
        pass
    m = Movie(title = data['title'],
              canonicalTitle = data['canonical title'],
              year = data['year'],
              rating = data['rating'],
              plot = data['plot'],
              plotOutline = data['plot outline'],
              mpaa = data['mpaa'],
              runtimes = data['runtimes'],
              cover = cover,
              imdbId = data['imdbId'],
              director = data['director'],
              cast = data['cast']
              )

    m.save()
    gs = [Genre.objects.get(name = g) for g in data['genres']]
    gs.append(Genre.objects.get(name = 'New'))
    gs.append(Genre.objects.get(name = 'All'))
    m.genres = gs
    m.save()

def import_test_movies():
    f = open('movie/test_movies.txt') #Placing this before genre import prevents
                            #genres being intialized multiple times if
                            #user enters a bad file name.

    import_all_genres() # Genre's must be intialized before loading movie data!
    print '- Genres successfully intialized -'

    for movie_id in f:
        import_movie(movie_id)

    print 'Movies COMPLETE'
