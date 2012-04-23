from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('dormbase.package.views',
    url(r'^$', 'package_get'),
    url(r'^add/$', 'package_add'),
    url(r'remove/$', 'package_remove')
)
