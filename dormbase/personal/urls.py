from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('dormbase.personal.views',
    url(r'^$', 'profile'),
    url(r'^(?P<username>.*)/$', 'profile_username')
)
