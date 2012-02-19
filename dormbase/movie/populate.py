import sys
sys.path.append('../contrib/IMDBpy')
import unicodedata
from imdb import IMDb
from dormbase.movie.models import Genre
from dormbase.movie.models import Movie


def initGenre():
    genreList = ['Action', 'Adventure', 'Animation', 'Biography',
                 'Comedy', 'Crime', 'Documentary', 'Drama',
                 'Family', 'Fantasy', 'Film-Noir', 'Game-Show',
                 'History', 'Horror', 'Music', 'Musical',
                 'Mystery', 'News', 'Reality-TV', 'Romance',
                 'Sci-Fi', 'Sport', 'Talk-Show', 'Thriller',
                 'War', 'Western', 'New'] # List was taken from IMDB genre page. 

    for i in genreList:
        g = Genre(name = i)
        g.save()

def movieData(movieID):
    data = {'title': '',
            'year': None,
            'rating': None,
            'plot': '',
            'plot outline': '',
            'genres': '',
            'mpaa': 'Mpaa not available.',
            'runtimes': '',
            'full-size cover url': ''}
    
    movie = IMDb().get_movie(movieID)

    title = unicodedata.normalize('NFKD', movie['title']).encode('ascii','ignore')

    for key in data:
        if movie.has_key(key):
            if type(movie[key]) == type([]) and key != 'genres':
                movie[key] = movie[key][0]
        
            if type(movie[key]) == type(''):
                movie[key] = unicodedata.normalize('NFKD', movie[key]).encode('ascii','ignore')

            data[key] = movie[key]

        else:
            print 'Error! {} not available in {}'.format(key, title)

    m = Movie(title = data['title'],
              plot = data['plot'],
              plotOutline = data['plot outline'],
              mpaa = data['mpaa'],
              runtimes = data['runtimes'],
              coverUrl = data['full-size cover url'],
              rating = data['rating'],
              year = data['year']
              )

    m.save()

    gs = [Genre.objects.filter(name = g) for g in data['genres']]
    gs.append(Genre.objects.filter(name = 'New'))

    fg = []
    for g in gs: 
        if len(g) > 0: fg.append(g[0])
    m.genres = fg
    m.save()

def loadDb(filename):
    try:
        initGenre() # Genre's must be intialized before loading movie data!
        print 'Genres successfully intialized.'
    except:
        print 'ERROR! Unable to intialize genres!'

    f = open(filename, 'r')
    for movieId in f:
        try:
            movieData(movieId)
        except:
            print 'ERROR! {} is not an IMDB movie ID'.format(movieId)

    print '- END -'
