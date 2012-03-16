import sys
sys.path.append('../contrib/IMDBpy')
import unicodedata
from imdb import IMDb
from dormbase.movie.models import Genre
from dormbase.movie.models import Movie


def import_all_genres():
    genre_list = ['Action', 'Adventure', 'Animation', 'Biography',
                 'Comedy', 'Crime', 'Documentary', 'Drama',
                 'Family', 'Fantasy', 'Film-Noir', 'Game-Show',
                 'History', 'Horror', 'Music', 'Musical',
                 'Mystery', 'News', 'Reality-TV', 'Romance',
                 'Sci-Fi', 'Sport', 'Talk-Show', 'Thriller',
                 'War', 'Western', 'New'] # List was taken from IMDB genre page. 

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

    m = Movie(title = data['title'],
              canonicalTitle = data['canonical title'],
              year = data['year'],
              rating = data['rating'],
              plot = data['plot'],
              plotOutline = data['plot outline'],
              mpaa = data['mpaa'],
              runtimes = data['runtimes'],
              coverUrl = data['full-size cover url'],
              imdbId = data['imdbId'],
              director = data['director'],
              cast = data['cast']
              )

    m.save()
    gs = [Genre.objects.filter(name = g)[0] for g in data['genres']]
    gs.append(Genre.objects.filter(name = 'New')[0])
    m.genres = gs
    m.save()

def import_test_movies(filename):
    f = open('movie/test_movies.txt') #Placing this before genre import prevents
                            #genres being intialized multiple times if
                            #user enters a bad file name.

    import_all_genres() # Genre's must be intialized before loading movie data!
    print '- Genres successfully intialized -'

    for movie_id in f:
        import_movie(movie_id)

    print 'Movies COMPLETE'
