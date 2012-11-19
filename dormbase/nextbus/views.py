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
from lxml import etree
import datetime

# Info on Nextbus api:
# http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf

def nextbus(request):
    try:
        # Nextbus api: http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf
        baseURL = 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions'
        agency = 'mit'
        stop = 'simmhl'	#This should be a variable with proper dorm

        techURL = '{}&a={}&r={}&s={}'.format(baseURL, agency, 'tech', stop)
        saferideURL = '{}&a={}&r={}&s={}'.format(baseURL, agency, 'saferidecambwest', stop)

        techTimes = etree.parse(techURL).findall('predictions/direction/prediction')
        saferideTimes = etree.parse(saferideURL).findall('predictions/direction/prediction')

        # If techTimes is empty, then it isn't running, so check Saferide
        if techTimes:
            times = [i.get('minutes')+" "+getSuffix(i.get('minutes')) for i in techTimes]
            title = 'Tech Shuttle'
            stop_name = etree.parse(techURL).Element("predictions").get("stopTitle")
        elif saferideTimes:
            times =  [i.get('minutes')+" "+getSuffix(i.get('minutes')) for i in saferideTimes]
            title = 'Saferide Cambridge West'
        else:
            times = None
            title = 'Shuttle Unavailable'

    except Exception,e:
        times = [e,'','']   #Shouldn't happen but an error output is nice
        title = 'Shuttle Tracker Unavailable'

    nextbus_content = {'title':title,'times':[times[0],times[1],times[2]]}


    return render_to_response('nextbus/nextbus.html',nextbus_content,context_instance = RequestContext(request))

def getSuffix(time): #Because 1 mins just isn't going to cut it
    if(time == 1):
        return "min"
    else:
        return "mins"
