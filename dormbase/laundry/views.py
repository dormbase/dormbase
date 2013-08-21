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
import lxml.html

def laundry(request):
    lvs = lxml.html.parse('http://laundryview.com/lvs.php')
    div = lvs.find(".//div[@id='campus1']")
    rooms = []
    status = []
    for a in div.findall('.//a'):
        rooms.append(str(a.text).strip().title())
    for span in div.findall('.//span'):
        status.append(str(span.text).strip())

    pairs = dict(zip(rooms, status))

    allRooms = [x for x in pairs.keys() if x.startswith('Simmons')]

    simmons = {}

    for r in allRooms:
        simmons[r] = pairs[r]

    payload = {'laundry': simmons}

    print payload
    return render_to_response('laundry/laundry.html', payload, context_instance=RequestContext(request))
