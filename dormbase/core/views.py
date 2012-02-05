from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from dormbase.core.models import Resident
from dormbase.core.models import Room

from django.http import HttpResponse, HttpResponseRedirect, Http404
import json
import itertools

def user_to_dict(user):
    try:
        room, year = user.get_profile().room, user.get_profile().year
    except Resident.DoesNotExist:
        room, year = 'n/a', 'n/a'

    return {
        'id' : user.id,
        'username' : user.username,
        'firstname' : user.first_name,
        'lastname' : user.last_name,
        'room' : str(room), # force room to be serialized
        'year' : str(year),
    }

def resident_to_dict(resident):
    return {
        'id' : resident.user.id,
        'username' : resident.user.username,
        'firstname' : resident.user.first_name,
        'lastname' : resident.user.last_name,
        'room' : str(resident.room), # force room to be serialized
        'year' : str(resident.year),
    }

def room_to_dict(room):
    return map(resident_to_dict, Resident.objects.filter(room__id = room.id))

def directory(request):
    payload = {}
    return render_to_response('core/directory.html', request, payload)

def directory_json(request):
    results, resident_results, room_results = [], [], []
    retrieved_ids = []
    output = {}

    def one_not_empty(d, strings):
        return sum(len(d[s]) for s in strings) > 0

    def add_to_dict(d, results):
        for r in results:
            if not r['id'] in d:
                d[r['id']] = r
        return d
    
    if one_not_empty(request.GET, ['firstname', 'lastname', 'username']):
        results = map(user_to_dict, User.objects.filter(
            first_name__contains = request.GET['firstname']).filter(
            last_name__contains = request.GET['lastname']).filter(
            username__contains = request.GET['username'])[:10])
        retrieved_ids.append(map(lambda x: x['id'], results))
        output = add_to_dict(output, results)

    if one_not_empty(request.GET, ['title', 'year']):
        resident_results = map(resident_to_dict, Resident.objects.filter(
            title__contains = request.GET['title']).filter(
            year__contains = request.GET['year'])[:10])
        retrieved_ids.append(map(lambda x: x['id'], resident_results))
        output = add_to_dict(output, resident_results)
        
    if one_not_empty(request.GET, ['room']):
        room_results = map(room_to_dict, Room.objects.filter(
            number__startswith = request.GET['room'])[:10])
        # necessary because room_results goes through map() twice
        if len(room_results) > 0: room_results = room_results[0]
        retrieved_ids.append(map(lambda x: x['id'], room_results))
        output = add_to_dict(output, room_results)

    # early escape if only one query returned results
    if len(retrieved_ids) <= 1:
        jsons = json.dumps({'result' : list(results) + list(resident_results) + list(room_results)})
        return HttpResponse(jsons, mimetype='application/json')

    print retrieved_ids
    s = set(retrieved_ids[0])
    for idset in retrieved_ids[1:]:
        s = s.intersection(set(idset))

    final = []
    for id in s:
        final.extend([output[id]])
    
    jsons = json.dumps({'result' : final})
    return HttpResponse(jsons, mimetype='application/json')
