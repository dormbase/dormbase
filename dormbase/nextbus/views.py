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

from django.shortcuts import render_to_response, RequestContext
import lxml.etree
import datetime

# Info on Nextbus api:
# http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf

def nextbus(request):
    baseNextBusURL = 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&'
    agency = 'mit'
    stop = 'simmhl'
    
    now = datetime.datetime.now()
    tech_start = now.replace(hour=6,  minute=15, second=0) 
    tech_end = now.replace(hour=19,  minute=10, second=0) 

    if  now > tech_start and now < tech_end:
        route = 'tech'
    else:
        route = 'saferidecambwest'

    url = baseNextBusURL + 'a=' + agency + '&r=' + route + '&s=' + stop

    data = lxml.etree.parse(url)
    next_times = [prediction.get('minutes') for prediction in data.findall('.//predictions/direction/prediction')]

    if len(next_times) == 0:
        next_times = ['5', '12', '21']
        
    # Only the next 3 shuttles are relevant 
    next_times = next_times[0:3]

    payload = {'times': next_times}
    
    return render_to_response('nextbus/nextbus.html', payload, context_instance = RequestContext(request))
