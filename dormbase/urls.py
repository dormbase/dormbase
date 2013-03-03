# Dormbase -- open-source dormitory database system
# Copyright (C) 2012 Alex Chernyakhovsky <achernya@mit.edu>
#                    Drew Dennison       <dennison@mit.edu>
#                    Isaac Evans         <ine@mit.edu>
#                    Luke O'Malley       <omalley1@mit.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Home page
    url(r'^$', 'dormbase.views.home', name='home'),

    # Profile/Personal
    (r'^accounts/profile/', include('personal.urls')),

    # Registration
    (r'^accounts/', include('registration.backends.default.urls')),

    # Directory
    (r'^directory/', include('core.urls')),

    # Movie
    (r'^movies/', include('movie.urls')),

    # Desk
    (r'^desk/', include('desk.urls')),

    # Packages
    (r'package/', include('package.urls')),

    # Haystack
    (r'^search/', include('haystack.urls')),

    # Photologue
    (r'^photologue/', include('photologue.urls')),

    # Nextbus
    (r'^nextbus/', include('nextbus.urls')),

    # Menu
    (r'^menus/', include('menus.urls')),

    # Laundry
    (r'^laundry/', include('laundry.urls')),
    
    # Facilities
    (r'^facilities/', include('facilities.urls')),

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
