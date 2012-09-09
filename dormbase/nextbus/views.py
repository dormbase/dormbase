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

from django.shortcuts import render_to_response, RequestContext
import lxml.etree
import datetime

# Info on Nextbus api:
# http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf

def nextbus(request):
    try:
        # Nextbus api: http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf
        baseURL = 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions'
        agency = 'mit'
        stop = 'simmhl'

        techURL = '{}&a={}&r={}&s={}'.format(baseURL, agency, 'tech', stop)
        saferideURL = '{}&a={}&r={}&s={}'.format(baseURL, agency, 'saferidecambwest', stop)

        techTimes = etree.parse(techURL).findall('predictions/direction/prediction')
        saferideTimes = etree.parse(saferideURL).findall('predictions/direction/prediction')

        # If techTimes is empty, then it isn't running, so check Saferide
        if techTimes:
            times = [i.get('minutes') for i in techTimes]
            title = 'Tech Shuttle'
        elif saferideTimes:
            times =  [i.get('minutes') for i in saferideTimes]
            title = 'Saferide Cambridge West'
        else:
            # Fake times for testing
            times = ['NA', 'NA', 'NA']
            title = 'Unavailable'

    except:
        times = ['NA', 'NA', 'NA']
        title = 'Unavailable'
        
    out = {'title': title,
           'next': times[0],
           'second': times[1],
           'third': times[2]}
    
    return HttpResponse(json.dumps(out), mimetype="application/json")
