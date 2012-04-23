from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Home page
    url(r'^$', 'dormbase.views.home', name='home'),

    # Directory
    (r'^directory/', include('core.urls')),

    # Movie
    (r'^movies/', include('movie.urls')),

    # Profile/Personal
    (r'^personal/', include('personal.urls')),

    # Desk
    (r'^desk/', include('desk.urls')),

    # Packages
    (r'package/', include('package.urls')),

    # Haystack
    (r'^search/', include('haystack.urls')),

    # Photologue
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
