# Dormbase -- open-source dormitory database system
# Copyright (C) 2012 Alex Chernyakhovsky <achernya@mit.edu>
#                    Drew Dennison       <dennison@mit.edu>
#                    Isaac Evans         <ine@mit.edu>
#                    Luke O'Malley       <omalley1@mit.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import feedparser
import datetime
import lxml.html as html

def fix_bonapetit(thestr):
    """
    Horrible state-machine to parse the unhtmlified RSS feed and get
    the title and description.
    """
    food = {}
    last = ''
    build = ''
    for char in thestr:
        if char == '[':
            continue
        if char == ']':
            last = build
            build = ''
            continue
        if char == '\n':
            if build is not '':
                food[last.strip()] = build.strip()
                build = ''
            continue
        build += char
    return food
        
def menus(request):
    halls = [('Baker', '399'),
             ('Maseeh', '398'),
             ('McCormick', '400'),
             ('Next', '401'),
             ('Simmons', '402'),
             ]
    
    dorms_menus = {}
    day = datetime.datetime.now().weekday()

    for (dorm, i) in halls:
        # Make the URL and the Feed
        make_url = 'http://www.cafebonappetit.com/rss/menu/' + i

        try:
            raw_feed = feedparser.parse(make_url).entries[day]
            # Here we need to use lxml to parse the summary
            parser = html.fromstring(raw_feed.summary)
            # Now convert the summary into a text-version
            textversion = html.tostring(parser, method='text', encoding=unicode)
            # Fix the terrible RSS using a state-machine based parser,
            # removing weird UTF-8 characters on the way
            parsed_text = fix_bonapetit(textversion.replace(u'\xa0', ''))
            # Convery the resulting dictionary into a form that we can
            # send off to the template engine
            reformatted = []
            for (name, desc) in parsed_text.iteritems():
                reformatted.append({'name': name, 'description': desc})
        
            # Add this dorm food
                dorms_menus[dorm] = {'day': raw_feed.title_detail.value, 
                                     'meals': reformatted}
        except:
            dorms_menus[dorm] = {'day': 'This dining hall is closed today.',
                                 'meals': [],}

    payload = {'dorms': dorms_menus}

    return render_to_response('menus/menus.html', payload, 
                              context_instance = RequestContext(request))
