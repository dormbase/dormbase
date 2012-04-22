from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Directory
    url(r'^$', 'dormbase.views.home', name='home'),
    url(r'^directory$', 'dormbase.core.views.directory', name='directory'),
    url(r'^directory_json$', 'dormbase.core.views.directory_json', name='directory_json'),

    # Movie
    url(r'^movies/$', 'dormbase.movie.views.genre_random', name='directory_json'),
    url(r'^movie_reserve/$', 'dormbase.movie.views.movie_reserve'),
    url(r'^movies/genre/(?P<genreType>.*)/$', 'dormbase.movie.views.genre_list', name='movie_all'),
    url(r'^movies/detail/(?P<movieId>.*)/$', 'dormbase.movie.views.movie_detail', name='movie_detail'),

    # Profile
    url(r'^personal$', 'dormbase.personal.views.profile', name='personal'),

    # Desk
    url(r'^desk$', 'dormbase.desk.views.dashboard', name='desk'),
    url(r'^package_add/$', 'dormbase.package.views.package_add'),
    url(r'^package_remove/$', 'dormbase.package.views.package_remove'),

    # Haystack
    (r'^search/', include('haystack.urls')),
    (r'^photologue/', include('photologue.urls')),

    # Resources
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
             'document_root': settings.MEDIA_ROOT
             }), 

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{
             'document_root': settings.STATIC_ROOT,
             }),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
                       
)
urlpatterns += staticfiles_urlpatterns()
