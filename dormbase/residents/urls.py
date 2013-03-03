from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('dormbase.residents.views',
    url(r'^$', 'dashboard'),
    url(r'^(?P<username>.*)/$', 'profile_username')
)
