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

from django.contrib.auth.models import User
from dormbase.core.models import Resident
from dormbase.core.models import Room

from django.http import HttpResponse, HttpResponseRedirect, Http404
from haystack.query import SearchQuerySet

import json
import itertools

def directory(request):
    return render_to_response('core/directory.html', context_instance = RequestContext(request))

def directory_json(request):
    searchable_fields = ['firstname', 'lastname', 'username', 'year', 'room', 'title']
    search_args = {}
    for field in searchable_fields:
        if field in request.GET and len(request.GET[field]) > 1:
            search_args[field] = request.GET[field]

    search_results = None
    if 'term' in request.GET and len(request.GET['term']) > 1: # special case, general keyword search
        search_results = SearchQuerySet().filter(content = request.GET['term']).models(Resident)
    if len(search_args) > 0:
        search_results = SearchQuerySet().filter(**search_args).models(Resident)
    if search_results == None:
        return HttpResponse(json.dumps({'result': []}), mimetype='application/json')
    
    send_result = []
    for result in search_results:
        row = { field : result.get_stored_fields()[field] for field in searchable_fields[:-1] }
        send_result.append(row)

    jsons = json.dumps({'result' : send_result})
    return HttpResponse(jsons, mimetype='application/json')
