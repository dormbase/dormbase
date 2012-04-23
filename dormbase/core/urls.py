from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('dormbase.core.views',
    url(r'^$', 'directory'),
    url(r'^json/$', 'directory_json')
)
