from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

def profile(request):
    return render_to_response('personal/profile.html', context_instance = RequestContext(request))
