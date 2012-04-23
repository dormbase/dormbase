from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from dormbase.core.models import Resident
from django.http import Http404


def profile(request):
    return render_to_response('personal/profile.html', context_instance = RequestContext(request))

def profile_username(request, username):
    try:
        resident = Resident.objects.get(athena=username)  #need to query DB and get fullname
    except:
        raise Http404
    payload = {'fullname': resident.user.first_name + " " + resident.user.last_name,
               'room': resident.room, 'email': resident.athena + '@mit.edu',
               'phone': resident.cell, 'web': resident.url, 'about': resident.about,
               'year': resident.year }

    return render_to_response('personal/user.html', payload, context_instance = RequestContext(request))
