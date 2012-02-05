import sys
sys.path.append('../contrib/IMDBpy')

from imdb import IMDb
from dormbase.movie.models import Genre
from dormbase.movie.models import Movie


def initGenre():
    genreList = ['Action', 'Adventure', 'Animation', 'Biography',
                 'Comedy', 'Crime', 'Documentary', 'Drama',
                 'Family', 'Fantasy', 'Film-Noir', 'Game-Show'
                 'History', 'Horror', 'Music', 'Musical',
                 'Mystery', 'News', 'Reality-TV', 'Romance',
                 'Sci-Fi' 'Sport', 'Talk-Show', 'Thriller',
                 'War', 'Western']

    for i in genreList:
        g = Genre(name = i)
        g.save()

def movieData(movieID):
    data = {'title': '',
            'year': '',
            'rating': None,
            'plot': '',
            'plot outline': '',
            'genres': '',
            'mpaa': '',
            'runtimes': '',
            'full-size cover url': ''}
    
    movie = IMDb().get_movie(movieID)
    
    for key in data:
        try:
            data[key] = movie[key]
            # print data[key]
        except:
            print 'ERROR retrieving %s' %key

    m = Movie(title = data['title'],
                     year = data['year'],
                     plot = data['plot'],
                     plotOutline = data['plot outline'],
                     mpaa = data['mpaa'],
                     runtimes = data['runtimes'],
                     coverUrl = data['full-size cover url']
                     )

    if data['rating'] != None:
        m.rating = data['rating']
    
    m.save()
    gs = [Genre.objects.filter(name = g) for g in data['genres']]
    fg = []
    for g in gs: 
        if len(g) > 0: fg.append(g[0])
    m.genres = fg
    m.save()

def loadDb(filename):
    f = open(filename, 'r')
    for movieId in f:
        try:
            movieData(movieId)
        except:
            print "%s is not an IMDB movie ID" %s
