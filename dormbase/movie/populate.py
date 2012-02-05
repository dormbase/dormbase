import sys
sys.path.append('../contrib/IMDBpy')

from imdb import IMDb
from dormbase.movie.models import Genre
from dormbase.movie.models import Movie



def movieData(movieID):
    data = {'title': None,
            'year': None,
            'rating': '',
            'plot': None,
            'plot outline': None,
            'genres': None,
            'mpaa': '',
            'runtimes': '',
            'full-size cover url': None}
    
    movie = IMDb().get_movie(movieID)
    
    for key in data:
        try:
            data[key] = movie[key]
            # print data[key]
        except:
            print 'ERROR retrieving %s' %key

    m = Movie(title = data['title'],
                     year = data['year'],
                     rating = data['rating'],
                     plot = data['plot'],
                     plotOutline = data['plot outline'],
                     mpaa = data['mpaa'],
                     runtimes = data['runtimes'],
                     coverUrl = data['full-size cover url']
                     )
    
    m.save()
    gs = [Genre.objects.filter(name = g) for g in data['genres']]
    fg = []
    for g in gs: 
        if len(g) > 0: fg.append(g[0])
    m.genres = fg
    m.save()
