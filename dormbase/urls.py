from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dormbase.views.home', name='home'),
    url(r'^directory$', 'dormbase.core.views.directory', name='directory'),
    url(r'^directory_json$', 'dormbase.core.views.directory_json', name='directory_json'),
#    url(r'^directory_populate$', 'dormbase.core.views.populate_directory', name='populate'),
    url(r'^movies/$', 'dormbase.movie.views.randomGenre', name='directory_json'),
    url(r'^movies/genre/(?P<genreType>.*)/$', 'dormbase.movie.views.listGenre', name='movie_all'),
    url(r'^movies/detail/(?P<movieId>.*)/$', 'dormbase.movie.views.movieDetail', name='movie_detail'),
    url(r'^personal$', 'dormbase.personal.views.profile', name='personal'),
    url(r'^desk$', 'dormbase.desk.views.dashboard', name='desk'),

    # url(r'^movies$', 'dormbase.movie.views.list_movies', name='directory_json'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
             'document_root': settings.MEDIA_ROOT
             }), 

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{
             'document_root': settings.STATIC_ROOT,
             }),

    # url(r'^$', 'dormbase.views.home', name='home'),
    # url(r'^dormbase/', include('dormbase.foo.urls')),
    url(r'^directory$', 'dormbase.core.views.directory', name='directory'),
    url(r'^directory_json$', 'dormbase.core.views.directory_json', name='directory_json'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
                       
)
urlpatterns += staticfiles_urlpatterns()
