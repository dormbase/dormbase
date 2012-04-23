from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('dormbase.desk.views',
    url(r'^$', 'dashboard')
)
