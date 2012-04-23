from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('dormbase.movie.views',
    url(r'^$', 'genre_random'),
    url(r'^reserve/$', 'movie_reserve'),
    url(r'^genre/(?P<genreType>.*)/$', 'genre_list'),
    url(r'^detail/(?P<movieId>.*)/$', 'movie_detail')
)
