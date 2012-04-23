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
