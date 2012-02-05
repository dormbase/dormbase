import sys
sys.path.append('../contrib/IMDBpy')

from imdb import IMDb
import models

def movieData(movieID):
    data = {'title': None,
            'year': None,
            'rating': None,
            'plot': None,
            'plot outline': None,
            'genres': None,
            'mpaa': None,
            'runtimes': None,
            'full-size cover url': None}
    
    movie = IMDb().get_movie(movieID)
    
    for key in data:
        try:
            data[key] = movie[key]
            # print data[key]
        except:
            print 'ERROR importing IMDB data'


models.Movie(**data)

            
